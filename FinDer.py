from tkPlus.messagebox import showerror, showinfo
from modified_ttkbootstrap import *

str1 = str2 = str()


def create(find2=None, change=None):
    global e1, e2, top
    top = Toplevel()
    top.title("查找")
    # 设置顶层窗口的大小不可变
    top.maxsize(230, 60)
    top.minsize(230, 60)

    # 两个按钮和两个Entry输入框
    e1 = Entry(top)
    e1.grid(row=0, column=0)
    Button(top, text="查找下一个", width=10, command=find1, bootstyle=(SUCCESS,)).grid(row=0, column=1)
    e2 = Entry(top)
    e2.grid(row=1, column=0)
    Button(top, text="查找全部", width=10, command=find2, bootstyle=(WARNING,)).grid(row=1, column=1)

    # 当顶层窗口关闭的时候，所有的设置还原
    top.protocol(name='WM_DELETE_WINDOW', func=change)
    return top


def find1():
    global x, li, num, text, str1, str2
    li = []
    Init()
    x = e1.get()
    if len(x) == 0:
        showerror('错误', '请输入内容')
        return

    str1 = x
    # 如果说当前的str1是新输入的，则num要从0开始查找
    if str2 != str1:
        num = 0
    # 用现在的值把之前的值覆盖
    str2 = str1
    fun()
    if len(li) == 0:
        showinfo("查找结果", "没有要查询的结果")
        return
    if num == len(li):  # 如果后面没有要查找的，则直接跳转到第一个继续
        showinfo("查找结束", "找不到%s了" % x)
        num = 0
        return
    # 获取当前颜色要变化的位置
    i = li[num]
    num += 1

    Init()
    k, t = i.split(".")
    t = str(len(x) + int(t))
    j = k + '.' + t
    text.tag_add("tag1", i, j)
    text.tag_config("tag1", background="yellow", foreground="blue")
    li = []


def find2():
    global x, li
    # 每次进行一次全部查找，一定要先把li列表初始化
    li = []
    Init()
    x = e2.get()
    if len(x) == 0:  # 如果说从输入框中得不到内容，则直接终止，不进行判断
        showerror("错误", "请输入内容")
        return
    fun()
    if len(li) == 0:  # 没有找到，直接终止即可
        showinfo("查找结果", "没有要查询的结果")
        return
    for i in li:
        k, t = i.split(".")
        # 加上字符串的长度，即判断能达到的位置
        t = str(len(x) + int(t))
        # 重新连接
        j = k + '.' + t
        # 加特殊的前景色和背景色
        text.tag_add("tag1", i, j)
        text.tag_config("tag1", background="yellow", foreground="blue")
    li = []


def Init():
    global text

    x = text.get("1.0", END)
    text.delete("1.0", END)
    # 重新插入文本
    text.insert(INSERT, x)


def fun():
    '查找所有满足条件的字符串'
    global x, li
    start = "1.0"
    while True:
        pos = text.search(x, start, stopindex=END)
        if not pos:  # 没有找到
            # if len(li) != 0:
            # print li
            break
        li.append(pos)
        # len(x) 避免一个字符被查找多次
        start = pos + "+%dc" % len(x)


def change():
    global top, text
    # 如果要关闭窗口，则获取Text组件中的所有文本，
    # 再重新输入，防止查找的结果对Text文本框产生影响，然后关闭即可
    Init()
    # 刷新，关闭顶层窗口
    top.withdraw()
