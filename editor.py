import _thread
import _tkinter
import builtins
import time
import pynput
import FinDer
import ReplAyser
import autotab
import line_number
from tkinter import *
from tkinter import scrolledtext

import tk_emoji
from modified_ttkbootstrap import *

from plugin import TitleObject

try:  # 调用idle进行高亮
    from idlelib.colorizer import ColorDelegator
    from idlelib.percolator import Percolator
except ImportError:  # 可能未安装IDLE
    ColorDelegator = Percolator = None


def get_new_editor(master, mc2, window, title_obj: TitleObject, mode, zt, is_py, i):
    global saved
    def check_for_saved():
        """检查是否已保存"""
        global added_ast  # 加过星号没有
        added_ast = False  # 没有添加
        while True:
            time.sleep(1)  # 不等待会卡
            try:
                if saved:
                    if added_ast:  # 没有添加星号就不要误删用户加的
                        window.title(title_obj.title_.lstrip("*"))
                        added_ast = False  # 去掉星号记忆
                else:
                    if not added_ast:
                        window.title("*" + title_obj.title_)  # 添加星号
                        added_ast = True  # 添加星号记忆
            except _tkinter.TclError:  # 窗口被关闭
                break  # 退出循环
            except NameError:pass

    # 设置text
    textbox = Frame(master)
    edit_frame = Canvas(textbox, height=600, width=800,
                        bg="white", highlightthickness=0)

    # 设置line
    text = scrolledtext.ScrolledText(edit_frame, height=100, wrap="none", spacing3=5,

                                     bg="white",
                                     bd=0, font=(zt, 14), undo=True, insertwidth=1)
    lln = line_number.LineNumber(window, text, edit_frame)
    window.line_text = lln.line_text
    text.config(width=window.winfo_width() - window.line_text.winfo_width(), )
    # 我试试用pyglet载入字体，这样不用安装hack字体ok
    # 设置事件
    lln.line_text.bind("<MouseWheel>", lln.wheel)
    lln.text.bind("<MouseWheel>", lln.wheel)
    lln.text.bind("<Control-v>", lambda e: lln.get_txt_thread())
    lln.text.bind("<Control-V>", lambda e: lln.get_txt_thread())
    # lln.text.bind("<Key>", lambda e: lln.get_txt_thread())
    lln.show_line()
    lln.get_txt_thread()

    # 定义菜单操作
    def copy():
        """复制"""
        kmp = pynput.keyboard.Key
        virtual_keyboard = pynput.keyboard.Controller()
        virtual_keyboard.press(kmp.ctrl)
        virtual_keyboard.press("c")
        virtual_keyboard.release("c")
        virtual_keyboard.release(kmp.ctrl)

    def paste():
        """粘贴"""
        kmp = pynput.keyboard.Key
        virtual_keyboard = pynput.keyboard.Controller()
        virtual_keyboard.press(kmp.ctrl)
        virtual_keyboard.press("v")
        virtual_keyboard.release("v")
        virtual_keyboard.release(kmp.ctrl)

    def cut():
        """剪切"""
        kmp = pynput.keyboard.Key
        virtual_keyboard = pynput.keyboard.Controller()
        virtual_keyboard.press(kmp.ctrl)
        virtual_keyboard.press("x")
        virtual_keyboard.release("x")
        virtual_keyboard.release(kmp.ctrl)

    def find():
        """查找"""
        FinDer.text = text
        top = FinDer.create(FinDer.find2, FinDer.change)
        top.attributes("-topmost", True)

    def replace():
        """替换"""
        window.coding = StringVar(window)
        replace_dlg = ReplAyser.ReplaceDialog(window, text)
        # replace_dlg.attributes("-topmost", True)
        replace_dlg.show()

    # 给text设置菜单
    text.menu = Menu(text)
    text.menu.add_command(label="复制（Ctrl+C）", command=copy)
    text.menu.add_command(label="粘贴（Ctrl+V）", command=paste)
    text.menu.add_command(label="剪切（Ctrl+X）", command=cut)
    text.menu.add_separator()
    text.menu.add_command(label="查找（Ctrl+F）", command=find)
    text.menu.add_command(label="替换（Ctrl+R）", command=replace)
    text.bind("<Button-3>", (lambda event: text.menu.post(window.winfo_x() + event.x, window.winfo_y() + event.y)))

    # 设置自动缩进
    autotab.enter = lambda: (lln.get_txt_thread())
    autotab.Taber(window, text)

    text.pack(side=LEFT)
    textbox.pack()

    # 设置scrollbar
    sb = text.vbar
    text.config(yscrollcommand=sb.set)
    sb.pack(side=RIGHT, fill=Y)

    # 定义滚动菜单项目
    def end():
        text.see(END)

    def start():
        text.see(float(1))

    # 设置滚动菜单
    sbmenu = Menu(window)

    sbmenu.add_command(label="滚动至此")
    sbmenu.add_separator()

    sbmenu.add_command(label="顶部", command=start)
    sbmenu.add_command(label="底部", command=end)
    sbmenu.add_separator()

    sbmenu.add_command(label="向上翻页")
    sbmenu.add_command(label="向下翻译")
    sbmenu.add_separator()

    sbmenu.add_command(label="向上滚动")
    sbmenu.add_command(label="向下滚动")

    sb.bind("<Button-3>", (lambda e: (sbmenu.post(e.x + sb.winfo_x(), e.y + window.winfo_y()))))

    # 位置待调整

    def on_modify(*args):
        global saved
        lln.get_txt_thread()
        saved = False
        # tkinter.messagebox.showinfo(".",str(saved)+str(added_ast))

    text.bind('<Key>', on_modify)

    '''def check_modified():
        """检查修改"""
        try:
            while True:
                tmp = text.get(float(1), tkinter.END)  # 获取全部
                time.sleep(1)  # 等待1秒
                if not tmp == text.get(float(1), tkinter.END):
                    on_modify()  # 修改了
        except Exception as e:
            tkinter.messagebox.showerror("错误", str(e))'''

    now = "py" if ".py" in mc2 else "html" # 扁平总比嵌套好

    # _thread.start_new_thread(check_modified, tuple())  # tkinter的傻逼事件没有用，自力更生吧
    global fileType
    if ColorDelegator and is_py:
        fileType = "py"
        colorobj = None
        # 设置代码高亮显示
        _codefilter = ColorDelegator()

        def defines():
            dics = {"foreground": "", "background": "white"}
            self = _codefilter
            self.tagdefs = {
                "COMMENT": {"foreground": "green", "background": "white"},
                "KEYWORD": {"foreground": "blue", "background": "white"},
                "BUILTIN": {"foreground": "gray", "background": "white"},
                "STRING": {"foreground": "green", "background": "white"},
                "DEFINITION": {"foreground": "purple", "background": "white"},
                "SYNC": {'background': "pink", 'foreground': "red"},
                "TODO": {'background': "pink", 'foreground': "red"},
                "ERROR": {"foreground": "red", "background": "white"},
                # The following is used by ReplaceDialog:
                "hit": {"foreground": None, "background": "white"},
            }

            # if DEBUG: print('tagdefs', self.tagdefs)

        _codefilter.LoadTagDefs = defines
        if not colorobj:
            colorobj = Percolator(text)
        colorobj.insertfilter(_codefilter)
    elif ".htm" in mc2:
        fileType = "html"
        text.config(fg="blue")
        # 代码高亮（text后）
        # fileType = "py"
        colorobj = None
        # 设置代码高亮显示
        _codefilter = ColorDelegator()

        def defines():
            dics = {"foreground": "", "background": "white"}
            self = _codefilter
            self.tagdefs = {
                "COMMENT": {"foreground": "green", "background": "white"},
                "KEYWORD": {"foreground": "blue", "background": "white"},
                "BUILTIN": {"foreground": "gray", "background": "white"},
                "STRING": {"foreground": "green", "background": "white"},
                "DEFINITION": {"foreground": "purple", "background": "white"},
                "SYNC": {'background': "pink", 'foreground': "red"},
                "TODO": {'background': "pink", 'foreground': "red"},
                "ERROR": {"foreground": "red", "background": "white"},
                # The following is used by ReplaceDialog:
                "hit": {"foreground": None, "background": "white"},
            }

        # if DEBUG: print('tagdefs', self.tagdefs)

        _codefilter.LoadTagDefs = defines
        if not colorobj:
            colorobj = Percolator(text)
        colorobj.insertfilter(_codefilter)

    _thread.start_new_thread(check_for_saved, tuple())  # 启动检查星号进程
    if mode == 0 and now == "py":  # 示例代码
        texts = i
    elif mode == 0 and now == "html":
        texts = '''<html>
            <head>
                <meta charset="utf-8">
                <title>欢迎使用pyfactory编辑器</title>
            </head>
            <body>
                欢迎使用pyfactory编辑器
            </body>
    </html>'''
    else:  # 已写入代码
        texts = builtins.open(mc2, "r+", encoding="utf-8").read()
    text.insert(1.0, tk_emoji.with_surrogates(texts))

    textbox.now_file = mc2
    textbox.text = text

    return textbox, text, now, mc2
