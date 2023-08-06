import os
import re

from modified_ttkbootstrap import *
from tkinter import Frame, Label
from tkinter.constants import *
import modified_ttkbootstrap as ttk
from tkPlus import messagebox as msgbox


def handle(err, parent=None):
    # 用于处理错误
    # showinfo()中,parent参数指定消息框的父窗口
    msgbox.showinfo("错误", type(err).__name__ + ': ' + str(err), parent=parent)


def to_escape_str(byte):
    # 将字节(bytes)转换为转义字符串
    str = '';
    length = 1024
    for i in range(0, len(byte), length):
        str += repr(byte[i: i + length])[2:-1]
        str += '\n'
    return str


def to_bytes(escape_str):
    # 将转义字符串转换为字节
    # -*****- 1.2.5版更新: 忽略二进制模式中文字的换行符
    escape_str = escape_str.replace('\n', '')
    escape_str = escape_str.replace('"""', '\\"\\"\\"')  # 避免引号导致的SyntaxError
    escape_str = escape_str.replace("'''", "\\'\\'\\'")
    try:
        return eval('b"""' + escape_str + '"""')
    except SyntaxError:
        return eval("b'''" + escape_str + "'''")


def bell_(*args):
    msgbox.showwarning("啥也没有欸...", "如题")


class SearchDialog(Toplevel):
    # 查找对话框
    def __init__(self, master, text):
        self.master = master
        self.text = text
        self.coding = self.master.coding.get()

    def init_window(self, title="查找"):
        Toplevel.__init__(self, self.master)
        self.title(title)
        self.attributes("-toolwindow", True)
        self.attributes("-topmost", True)
        # 当父窗口隐藏后，窗口也跟随父窗口隐藏
        self.transient(self.master)
        self.wm_protocol("WM_DELETE_WINDOW", self.onquit)

    def show(self):
        self.init_window()
        frame = Frame(self)
        ttk.Button(frame, text="查找下一个", command=self.search).pack()
        ttk.Button(frame, text="退出", command=self.onquit).pack()
        frame.pack(side=RIGHT, fill=Y)
        inputbox = Frame(self)
        Label(inputbox, text="查找内容:").pack(side=LEFT)
        self.keyword = StringVar(self.master)
        keyword = ttk.Entry(inputbox, textvariable=self.keyword)
        keyword.pack(side=LEFT, expand=True, fill=X)
        keyword.bind("<Key-Return>", self.search)
        keyword.focus_force()
        inputbox.pack(fill=X)
        options = Frame(self)
        self.create_options(options)
        options.pack(fill=X)

    def create_options(self, master):
        Label(master, text="选项: ").pack(side=LEFT)
        self.use_regexpr = IntVar(self.master)
        ttk.Checkbutton(master, text="使用正则表达式", variable=self.use_regexpr) \
            .pack(side=LEFT)
        self.match_case = IntVar(self.master)
        ttk.Checkbutton(master, text="区分大小写", variable=self.match_case) \
            .pack(side=LEFT)
        self.use_escape_char = IntVar(self.master)
        self.use_escape_char.set(self.master.isbinary)
        ttk.Checkbutton(master, text="使用转义字符", variable=self.use_escape_char) \
            .pack(side=LEFT)

    def search(self, event=None, mark=True, bell=True):
        text = self.text
        key = self.keyword.get()
        if not key: return
        # 验证用户输入是否正常
        if self.use_escape_char.get():
            try:
                key = str(to_bytes(key), encoding=self.coding)
            except Exception as err:
                handle(err, parent=self)
                return
        if self.use_regexpr.get():
            try:
                re.compile(key)
            except re.error as err:
                handle(err, parent=self)
                return
        # 默认从当前光标位置开始查找
        pos = text.search(key, INSERT, 'end-1c',  # end-1c:忽略末尾换行符
                          regexp=self.use_regexpr.get(),
                          nocase=not self.match_case.get())
        if not pos:
            # 尝试从开头循环查找
            pos = text.search(key, '1.0', 'end-1c',
                              regexp=self.use_regexpr.get(),
                              nocase=not self.match_case.get())
        if pos:
            if self.use_regexpr.get():  # 获取正则表达式匹配的字符串长度
                text_after = text.get(pos, END)
                flag = re.IGNORECASE if not self.match_case.get() else 0
                length = re.match(key, text_after, flag).span()[1]
            else:
                length = len(key)
            newpos = "%s+%dc" % (pos, length)
            text.mark_set(INSERT, newpos)
            if mark: self.mark_text(pos, newpos)
            return pos, newpos
        elif bell:  # 未找到,返回None
            bell_(widget=self)

    def findnext(self, cursor_pos='end', mark=True, bell=True):
        # cursor_pos:标记文本后将光标放在找到文本开头还是末尾
        # 因为search()默认从当前光标位置开始查找
        # end 用于查找下一个操作, start 用于替换操作
        result = self.search(mark=mark, bell=bell)
        if not result: return
        if cursor_pos == 'end':
            self.text.mark_set('insert', result[1])
        elif cursor_pos == 'start':
            self.text.mark_set('insert', result[0])
        return result

    def mark_text(self, start_pos, end_pos):
        text = self.text
        text.tag_remove("sel", "1.0", END)  # 移除旧的tag
        # 已知问题: 代码高亮显示时, 无法突出显示找到的文字
        text.tag_add("sel", start_pos, end_pos)  # 添加新的tag
        lines = text.get('1.0', END)[:-1].count(os.linesep) + 1
        lineno = int(start_pos.split('.')[0])
        # 滚动文本框, 使被找到的内容显示 ( 由于只判断行数, 已知有bug); 另外, text['height']不会随文本框缩放而变化
        text.yview('moveto', str((lineno - text['height']) / lines))
        text.focus_force()
        self.master.update_status()

    def onquit(self):
        self.withdraw()


class ReplaceDialog(SearchDialog):
    # 替换对话框
    def show(self):
        self.init_window(title="替换")
        frame = Frame(self)
        ttk.Button(frame, text="查找下一个", command=self._findnext).pack()
        ttk.Button(frame, text="替换", command=self.replace).pack()
        ttk.Button(frame, text="全部替换", command=self.replace_all).pack()
        ttk.Button(frame, text="退出", command=self.onquit).pack()
        frame.pack(side=RIGHT, fill=Y)

        inputbox = Frame(self)
        Label(inputbox, text="查找内容:").pack(side=LEFT)
        self.keyword = StringVar(self.master)
        keyword = ttk.Entry(inputbox, textvariable=self.keyword)
        keyword.pack(side=LEFT, expand=True, fill=X)
        keyword.focus_force()
        inputbox.pack(fill=X)

        replace = Frame(self)
        Label(replace, text="替换为:  ").pack(side=LEFT)
        self.text_to_replace = StringVar(self.master)
        replace_text = ttk.Entry(replace, textvariable=self.text_to_replace)
        replace_text.pack(side=LEFT, expand=True, fill=X)
        replace_text.bind("<Key-Return>", self.replace)
        replace.pack(fill=X)

        options = Frame(self)
        self.create_options(options)
        options.pack(fill=X)

    def _findnext(self):  # 仅用于"查找下一个"按钮功能
        text = self.text
        sel_range = text.tag_ranges('sel')  # 获得选区的起点和终点
        if sel_range:
            selectarea = sel_range[0].string, sel_range[1].string
            result = self.findnext('start')
            if result is None: return
            if result[0] == selectarea[0]:  # 若仍停留在原位置
                text.mark_set('insert', result[1])  # 从选区终点继续查找
                self.findnext('start')
        else:
            self.findnext('start')

    def replace(self, bell=True, mark=True):
        text = self.text
        result = self.search(mark=False, bell=bell)
        if not result: return  # 标志已无文本可替换
        # self.master.text_change()
        pos, newpos = result
        newtext = self.text_to_replace.get()
        try:
            if self.use_escape_char.get():
                newtext = to_bytes(newtext).decode(self.master.coding.get())
            if self.use_regexpr.get():
                old = text.get(pos, newpos)
                newtext = re.sub(self.keyword.get(), newtext, old)
        except Exception as err:
            handle(err, parent=self);
            return
        text.delete(pos, newpos)
        text.insert(pos, newtext)
        end_pos = "%s+%dc" % (pos, len(newtext))
        if mark: self.mark_text(pos, end_pos)
        return pos, end_pos

    def replace_all(self):
        self.text.mark_set("insert", "1.0")  # 将光标移到开头
        flag = False  # 标志是否已有文字被替换

        # 以下代码会导致无限替换, 使程序卡死, 新的代码修复了该bug
        # while self.replace(bell=False)!=-1:
        #    flag=True
        last = (0, 0)
        while True:
            result = self.replace(bell=False, mark=False)
            if result is None: break
            flag = True
            result = self.findnext('start', bell=False, mark=False)
            if result is None: return
            ln, col = result[0].split('.')
            ln = int(ln);
            col = int(col)
            # 判断新的偏移量是增加还是减小
            if ln < last[0] or (ln == last[0] and col < last[1]):
                self.mark_text(*result)  # 已完成一轮替换
                break
            last = ln, col
        if not flag: bell_()


1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
