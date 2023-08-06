# 导库
import tkinter.ttk
import _thread
import builtins
import ctypes
import ntpath
import os
import sys
import time
import tkinter.messagebox
import traceback
import webbrowser
from tkinter import *
from tkinter import filedialog
from typing import AnyStr, Union



import pyglet
import pyperclip
import tkPlus.functions
import modified_ttkbootstrap
from pip._vendor import requests
from tkPlus import messagebox
from modified_ttkbootstrap import *
from modified_ttkbootstrap import Button
from modified_ttkbootstrap.constants import *

import editor
import font_selector
import notebookWithCloseBtn
import tk_emoji
from plugin import ScrollListbox, TitleObject, mkdir, mkfile

from startui import *

package = []
packages = []


zt = "Cascadia Code"
fg = "Black"
i = '''from time import *

# 以下是示例代码
print("欢迎使用奥利给Python编译器！！！")
sleep(5)
'''.replace("奥利给Python编译器", "PyFactory 3.0")

import tkinter_stat

VERSION = "3.0"
MS = 114

pyglet.font.load("./font/Hack.ttf")


class ModalWindow(tkinter.Toplevel):
    """模态框"""

    def __init__(self, m: Union[tkinter.Tk, tkinter.Toplevel] = None):
        """初始化"""
        tkinter.Toplevel.__init__(self)
        self.m = m
        if m:
            m.attributes("-disabled", True)
            self.wm_protocol("WM_DELETE_WINDOW", self.close)
            self.focus()

    def close(self):
        """关闭"""
        if self.m:
            self.m.attributes("-disabled", False)
        self.destroy()


try:  # 调用idle进行高亮
    from idlelib.colorizer import ColorDelegator
    from idlelib.percolator import Percolator
except ImportError:  # 可能未安装IDLE
    ColorDelegator = Percolator = None


# 函数区
def fz(nr):
    pyperclip.copy(nr)


def bzj(mc, xs, dm2):
    # 标准节
    # Label(mc, text=xs).pack()
    def dm():
        fz(dm2)

    Button(mc, text=xs, command=dm).pack()
    # 已上为标准节


def dmts():  # 代码提示
    win = Tk()
    win.f0cus = win.focus_force()
    canvas = Canvas(win, width=200, height=310000, scrollregion=(0, 0, 820, 820))  # 创建canvas
    dmts = Frame(canvas, height=100)  # 用框架换掉窗口，方便滚动
    win.title("代码词典")
    win.geometry("300x300")
    # sb = Scrollbar(dmts)
    # sb.pack(side=RIGHT, fill=Y)
    # 这个scrollbar没有用了，看下面那个
    Label(dmts, text="代码词典", font=20).pack()
    Label(dmts, text="点击按钮复制代码").pack()
    # 标准节
    # Label(dmts, text="print()，输出").pack()
    # def dm():
    #     fz("print()")
    # Button(dmts, text="复制代码", command=dm).pack()
    # 已上为标准节
    for i in range(6):
        Label(dmts, text="  ").pack()
    # Label(dmts, text="  ").pack()
    # Label(dmts, text="  ").pack()
    # Label(dmts, text="  ").pack()
    # Label(dmts, text="  ").pack()
    try:
        win.f0cus()
    except TypeError:
        print("垃圾功能已启动")
    # Label(dmts, text="  ").pack()

    bzj(dmts, "print()，输出", "print()")
    bzj(dmts, "input(),输入", "input()")
    bzj(dmts, "def():,定义函数", "def():")
    bzj(dmts, "if,判断语句", "if")
    bzj(dmts, "import,导库语句", "import")
    bzj(dmts, "from import*,导库", "from import*")
    bzj(dmts, "import math,导入math库", "import math")
    bzj(dmts, "math.pi, 圆周率，", "math.pi")
    bzj(dmts, "math.ceil(x), 对x向上取整", "math.ceil(x)")
    bzj(dmts, "math.floor(x), 对x向下取整", "math.floor(x)")
    bzj(dmts, "math.pow(x), 对x向上取整", "math.pow(x)")
    bzj(dmts, "math.sqrt(x), x的平方根", "math.sqrt(x)")
    bzj(dmts, "from tkinter import*,导入tkinter库", "from tkinter import*")
    bzj(dmts, "= Tk(),创建窗口", "= Tk()")
    bzj(dmts, "Label(),标签", "Label()")
    bzj(dmts, "Button(),按钮", "Button()")
    bzj(dmts, "Entry(),输入框", "Entry()")
    bzj(dmts, "Text(),多行输入", "Text()")
    bzj(dmts, ".pack(),展示", ".pack()")
    bzj(dmts, "width=,宽", "width=")
    bzj(dmts, "height=,高", "height=")
    bzj(dmts, ".mainloop(),循环刷新", ".mainloop()")

    tkinter.Button(dmts, text="联机查看更多内容", command=open_link3, underline=1, borderwidth=0, fg="blue",
                   cursor="hand2", ).pack()

    vbar = Scrollbar(win, orient=VERTICAL, command=canvas.yview)  # 竖直滚动条
    vbar.place(x=280, y=0, height=300)
    canvas.config(yscrollcommand=vbar.set)
    dmts.pack()  # 显示控件
    canvas.pack()
    canvas.create_window((90, 240), window=dmts)  # create_window,让他们互相绑定
    win.mainloop()


def open_link3():
    """打开链接"""
    webbrowser.open("http://wry.ljcsunrise.tech/projects/pyfactory/code_dict.html")


def dkwy(wz):  # 打卡网址，wz=网址
    import webbrowser as w
    w.open(wz)


def bfyy(yy):
    r"""import os
    import easygui
    xzjg = easygui.ccbox("选择查找的位置", title="选择位置", choices=["本地", "QQ音乐"])
    # file = r"D:\User\Dashujv\语音分析\data\声声慢.wav"
    if xzjg:
        os.system(yy)
    else:
        os.system(f"start https://y.qq.com/n/ryqq/search?w={yy}&t=song&remoteplace=txt.yqq.top")"""
    tkinter.messagebox.showwarning("功能已关闭", "鉴于该功能没有任何用处，我们已关闭音乐功能，敬请谅解！")


def yy():
    """
    yy = Toplevel()
    yy.title("放点音乐")
    yy.geometry("250x250")
    yy.focus()
    Label(yy, text="请输入音乐名称").pack()
    yymc = tkPlus.functions.EntryWithPlaceholder(yy, placeholder="输入以在QQ音乐进行搜索，可能需要VIP...")
    yymc.pack()

    def bfyy2():
        if not yymc.get() or yymc.get() == "输入以在QQ音乐进行搜索，可能需要VIP...":
            messagebox.messagebox.showerror("错误", "不输入音乐名称怎么播放？")
            return  # 停止
        bfyy(yymc.get())

    Button(yy, text="播放此音乐", command=bfyy2, ).pack()

    def drown():
        dkwy("https://y.qq.com/n/ryqq/songDetail/261435364")

    def STAY():
        dkwy("https://y.qq.com/n/ryqq/songDetail/0043EX2e2F6JCA")

    Button(yy, text="推荐音乐：drown", command=drown).pack()
    Button(yy, text="推荐音乐：STAY", command=STAY).pack()
    yy.mainloop()
    """
    tkinter.messagebox.showwarning("功能已关闭", "鉴于该功能没有任何用处，我们已关闭音乐功能，敬请谅解！")


def kgl():
    global package, packages

    # 函数区
    def execCmd(cmd):
        r = os.popen(cmd)
        text = r.read()
        r.close()
        return text

    global kgl_window

    def install_package():
        def install(call=None):
            package_name = package_name_entry.get()
            os.system("start python -m pip install " + package_name)
            inspack_window.destroy()

        inspack_window = Toplevel()
        inspack_window.title("安装库")
        inspack_window.geometry("325x350")

        Label(inspack_window, text="安装库").pack()

        package_name_entry = Entry(inspack_window)
        package_name_entry.bind("<Return>", install)
        package_name_entry.pack()

        submit_button = Button(inspack_window, text="安装！！！", command=install)
        submit_button.pack()

        inspack_window.mainloop()

    def delete_package():
        package_index = lb1.curselection()
        for i in package_index:
            package_name = packages[i][0]
            os.system("start python -m pip uninstall -y " + package_name)

    def update_package():
        package_index = lb1.curselection()
        for i in package_index:
            package_name = packages[i][0]
            os.system("start python -m pip install --upgrade " + package_name)

    def get_packages():
        global package, packages

        text = execCmd("python -m pip list")
        package = text.split("\n")[2:-1]
        packages = []
        for i in package:
            _1 = ""
            for j in i:
                if j == " ":
                    break
                else:
                    _1 = _1 + j
            _2 = i.replace(" ", "")
            _2 = _2.replace(_1, "")
            packages.append([_1, _2])

        # [["package name", "package version"], ......]

        packages = packages[:]

        return packages

    def update_window():
        old_packages = packages
        if old_packages != get_packages():
            lb1.delete(0, END)
            for i in package:
                lb1.insert("end", i)

        kgl_window.after(MS, update_window)

    package = []
    packages = []

    kgl_window = Toplevel()
    kgl_window.title("库管理")
    kgl_window.geometry("320x370")

    Label(kgl_window, text="库管理").pack()

    frame = Frame(kgl_window)

    sb = Scrollbar(frame)
    dasb = Scrollbar(frame, orient=HORIZONTAL)
    sb.pack(side=RIGHT, fill="y")
    dasb.pack(side=BOTTOM, fill="x")

    lb1 = Listbox(frame, yscrollcommand=sb.set, xscrollcommand=dasb.set)
    lb1.pack(side=LEFT, fill="both")

    sb.config(command=lb1.yview)
    dasb.config(command=lb1.xview)
    frame.pack()

    btn1 = Button(kgl_window, text="安装库", bootstyle=SUCCESS, command=install_package)
    btn1.pack()
    Label(kgl_window).pack()  # 撑大点
    btn2 = Button(kgl_window, text="更新", bootstyle=PRIMARY, command=update_package)
    btn2.pack()

    Label(kgl_window).pack()  # 撑大点
    btn3 = Button(kgl_window, text=""
                                   "卸载", bootstyle=DANGER, command=delete_package)
    btn3.pack()

    global statbar
    statbar = tkinter_stat.StatusBar(kgl_window, status="正在加载...")
    statbar.pack()

    kgl_window.focus_force()
    kgl_window.update()
    update_window()

    statbar.config(status="准备就绪...")
    kgl_window.mainloop()


class Getter(object):
    def __init__(self, none): pass

    def pack(self): pass

    def get(self):
        """获取"""
        return filedialog.askopenfilename(title="打开文件",
                                          filetypes=[("Python源码", "*.py"), ("Python纯UI源码", "*.pyw"),
                                                     ("HTML5", "*.html"), ("CSS3", "*.css"),
                                                     ("javascript", "*.js"), ("其他", "*.*")])


def dqwj():
    zck = None
    # Label(zck, text="请输入文件名称", font=20).pack()
    global mc
    mc = Getter(zck)
    mc.pack()
    xjbc(1)

    '''
        def yx():
            a = text.get("1.0", "end")
            with open(mc2, "w", encoding="UTF-8") as file:
                file.write(a)
            dm = "python " + mc2
            os.system(dm)

        def bc():
            a = text.get("1.0", "end")
            with open(mc2, "w", encoding="UTF-8") as file:
                file.write(a)

        def dq():
            with open(mc2, "r", encoding="UTF-8") as file:
                wj = file.read()
                return wj

        # 插入文本
        texts = dq()
        text.insert(1.0, texts)
        # 按钮
        Button(window, text="运行程序", command=yx).pack(side=RIGHT)
        Button(window, text="保存代码", command=bc).pack(side=RIGHT)
        Button(window, text="库管理", command=kgl).pack(side=LEFT)
        Button(window, text="背景音乐", command=yy).pack(side=LEFT)
        Button(window, text="代码提示", command=dmts).pack(side=LEFT)
        window.mainloop()
    '''


def xjwj():
    zck = Toplevel()
    zck.f = zck.focus_force
    zck.title("新建文件")
    zck.geometry("250x250")
    Label(zck, text="请输入文件名称", font=20).pack()
    global mc
    mc = tkPlus.functions.EntryWithPlaceholder(zck, placeholder="输入文件路径...")
    mc.pack()

    def selfile():
        nam = filedialog.asksaveasfilename(
            title="选择保存路径",
            filetypes=[("Python源码", "*.py"),
                       ("Python纯UI源码", "*.pyw"),
                       ("HTML5", "*.html"),
                       ("CSS3", "*.css"),
                       ("javascript", "*.js"),
                       ("其他", "*.*")  # 我搜索一下ok可以了还是不行 怎么回事bzd  这个先搁着，以后再说
                       ],
            defaultextension=".py"
        )
        if not "." in nam:
            nam = nam + ".py"
        zck.focus()
        mc.focus_force()
        zck.update()
        # time.sleep(1)
        mc.delete(0, END)
        print(nam)
        mc.insert(END,
                  nam)

    browse = Button(zck, text="浏览...", bootstyle=(SUCCESS), command=selfile)
    zck.f()
    browse.pack()
    Button(zck, text="创建文件", command=lambda: xjbc(0)).pack()

    zck.mainloop()


# 代码编辑器
# noinspection DuplicatedCode
def xjbc(mode):
    # 主窗口
    mc2 = mc.get()
    is_py = ".py" in mc2
    if not ntpath.exists("untitleds.txt"):
        with builtins.open("untitleds.txt", "w+") as f:
            f.write("0")
        f.close()
        x = 0
    else:
        with builtins.open("untitleds.txt", "r+") as f1:
            try:
                x = int(f1.read())
            except TypeError:
                messagebox.showerror("无法读配置文件", "请删除untitleds.txt重试！")
                return  # 结束函数
            with builtins.open("untitleds.txt", "w+") as f2:
                f2.write(str(x + 1))  # 写入更大的数字
            f2.close()  # 关闭文件
        f1.close()  # 关闭文件
    if mc2 == "输入文件路径..." or not mc2:
        mc2 = "未命名" + str(x) + ".py"  # 默认名称
    global saved, window, files, file_abs_list
    saved = True
    window = Toplevel()
    old = window.title

    def title(title: AnyStr):
        """替换掉title（）（有记忆功能）"""
        global title_
        title_ = title
        title_obj.title_ = title_
        old(title)

    def yx():
        _thread.start_new_thread(_yx, tuple())

    def _yx():
        if now == "py":  # Python运行
            a = text.get("1.0", "end")
            with open(mc2, "w", encoding="UTF-8") as file:
                file.write(a)
            file.close()  # 关闭文件
            dm = "ConsolePauser python \"" + mc2 + "\""
            os.system(dm)
        else:  # HTML运行
            a = text.get(float(1), tkinter.END)
            with open(mc2, "w", encoding="UTF-8") as file:
                file.write(a)
            file.close()  # 关闭文件
            webbrowser.open(ntpath.join(os.getcwd(), mc2))  # 浏览器打开

    def bc():
        now_editor_widget = window.nametowidget(editor_tab.select())
        a = now_editor_widget.text.get("1.0", "end")
        mc2 = now_editor_widget.now_file
        try:
            with open(mc2, "w", encoding="UTF-8") as file:
                file.write(a)
            file.close()
        except Exception as e:
            messagebox.showerror("错误",
                                 "保存文件出现错误，请联系开发团队邮箱：wry_beiyong06@outlook.com QQ用户请使用关于的QQ号添加\n错误代码：" + e.__str__())
            return  # 直接返回
        global saved
        saved = True  # 返回到True状态

    def update_files():
        global files, file_abs_list
        files_dig.lb1.delete(0, END)

        files = []
        file_abs_list = []

        def get_Path(path):
            global files, file_abs_list
            try:
                file_or_dir = os.listdir(path)
            except:
                file_or_dir = []

            for file_dir in file_or_dir:
                file_or_dir_path = os.path.join(path, file_dir)
                if os.path.isdir(file_or_dir_path):
                    file_name = os.path.join(path, file_or_dir_path).replace(file_info[0] + "\\", "")
                    if file_name[0] != ".":
                        file_abs_list.append(file_name)
                        file_qg_count = file_name.count("\\") + file_name.count('/')

                        if file_qg_count != 0:
                            file_white_space = (file_qg_count + 1) * "  "
                            file_new_name = file_name[file_name.rindex('\\') + 1:]
                        else:
                            file_white_space = "  "
                            file_new_name = file_name

                        files.append(file_white_space + tk_emoji.with_surrogates("📁") + file_new_name)

                        get_Path(file_or_dir_path)
                else:
                    pass

            get_file(path)

        def get_file(path):
            global files, file_abs_list
            try:
                file_or_dir = os.listdir(path)
            except PermissionError:
                file_or_dir = []
                return file_or_dir
            for file_dir in file_or_dir:
                file_or_dir_path = os.path.join(path, file_dir)
                if os.path.isdir(file_or_dir_path):
                    pass
                else:
                    file_name = os.path.join(path, file_or_dir_path).replace(file_info[0] + "\\", "")
                    if file_name[0] != ".":
                        file_abs_list.append(file_name)
                        file_qg_count = file_name.count("\\") + file_name.count('/')

                        if file_qg_count != 0:
                            file_white_space = (file_qg_count + 1) * "  "
                            file_new_name = file_name[file_name.rindex('\\') + 1:]
                        else:
                            file_white_space = "  "
                            file_new_name = file_name

                        files.append(file_white_space + tk_emoji.with_surrogates("📄") + file_new_name)

        try:  # 问题解决了，我把ttkbootstrap改了，给notebook开了个后门，就不会覆盖主题了。你可以接着搞你那个功能了
            try:
                file_path_index = file_info[0].rindex("\\")
            except ValueError:
                file_path_index = file_info[0].rindex("/")
        except ValueError:
            return  # messagebox.showerror("路径错误", "请选择或浏览完整的路径")
        file_new_name = file_info[0][file_path_index + 1:]
        files.append("" + tk_emoji.with_surrogates("📁") + file_new_name)
        file_abs_list.append(file_info[0])

        get_Path(file_info[0])

        for f in files:
            files_dig.lb1.insert(END, f)

    def create_dir():
        try:
            file_in_list_index = files_dig.lb1.curselection()
            file_name_has_emoji = files[file_in_list_index[0]]
            file_abs = file_abs_list[file_in_list_index[0]]
            try:
                emoji_index = file_name_has_emoji.index(tk_emoji.with_surrogates("📄"))
            except:
                folder_path = file_abs
            else:
                messagebox.showerror("错误", "喂，怎么在文件里新建文件夹？？？")
                return
            def action():
                name = file_abs + "/" + dir_name.get()

                if mkdir(os.path.join(file_info[0], name)):
                    messagebox.showinfo("提示", "目录创建成功")
                else:
                    messagebox.showerror("错误", "目录创建失败")

                create_dir_window.destroy()
                _thread.start_new_thread(update_files, ())


            create_dir_window = Toplevel()

            Label(create_dir_window, text='创建目录').pack()

            dir_name = Entry(create_dir_window)
            dir_name.pack()

            submit = Button(create_dir_window, text='创建', command=action)
            submit.pack()

            create_dir_window.mainloop()
        except:
            messagebox.showerror("错误", "你好像没有选择文件或文件夹")

    def create_file():
        try:
            file_in_list_index = files_dig.lb1.curselection()
            file_name_has_emoji = files[file_in_list_index[0]]
            file_abs = file_abs_list[file_in_list_index[0]]
            try:
                emoji_index = file_name_has_emoji.index(tk_emoji.with_surrogates("📄"))
            except:
                folder_path = file_abs
            else:
                messagebox.showerror("错误", "喂，怎么在文件里新建文件？？？")
                return

            def action():
                name = file_abs + "/" + dir_name.get()


                if mkfile(os.path.join(file_info[0], name)):
                    messagebox.showinfo("提示", "文件创建成功")
                else:
                    messagebox.showerror("错误", "文件创建失败")

                create_file_window.destroy()
                _thread.start_new_thread(update_files, ())

            create_file_window = Toplevel()

            Label(create_file_window, text='创建文件').pack()

            dir_name = Entry(create_file_window)
            dir_name.pack()

            submit = Button(create_file_window, text='创建', command=action)
            submit.pack()

            create_file_window.mainloop()
        except:
            messagebox.showerror("错误", "你好像没有选择文件或文件夹")

    def open_file(event=None):
        global now_editor
        file_in_list_index = files_dig.lb1.curselection()
        file_name_has_emoji = files[file_in_list_index[0]]
        file_abs = file_abs_list[file_in_list_index[0]]
        try:
            emoji_index = file_name_has_emoji.index(tk_emoji.with_surrogates("📄"))
        except:
            # messagebox.showerror("错误", "喂，文件夹怎么打开")
            # emoji_index=file_name_has_emoji.index(tk_emoji.with_surrogates("📁"))
            sbfuck = "start explorer \"" + file_abs + "\""
            os.system(sbfuck)
            return
        else:
            file_name = file_name_has_emoji[emoji_index + 2:]
            if not "." in file_name:
                messagebox.showerror("错误", "喂，怎么打开没后缀的文件？？？")
                return
            else:
                file_ext_name = os.path.splitext(file_name)[1]
                is_py = file_ext_name == ".py"
                is_html = (file_ext_name == ".html") or (file_ext_name == ".htm")
                if is_py or is_html:
                    file_path = os.path.join(file_info[0], file_abs)
                    new_editor = editor.get_new_editor(editor_tab, file_path, window, title_obj,
                                                       1, zt, is_py, i)
                    editor_tab.add(new_editor[0], text=file_name)
                    editor_tab.select(new_editor[0])
                    now_editor = new_editor
                else:
                    messagebox.showerror("错误", "不是.py和.html、.htm怎么打开？不支持！")
                    return

    def delete_action():
        file_in_list_index = files_dig.lb1.curselection()
        file_abs = file_abs_list[file_in_list_index[0]]
        os.remove(os.path.join(file_info[0], file_abs))
        _thread.start_new_thread(update_files, tuple())

    def close_window():
        editor_tab.destroy()
        window.destroy()

    file_info = os.path.split(mc2)

    title_obj = TitleObject()

    window.title = title  # 替换
    window.title(file_info[1] + " - PyFactory2")
    window.f = window.focus

    files_frame = Frame(window)

    files_dig = ScrollListbox(files_frame)
    files_dig.pack()

    file_update_button = Button(files_frame, text="更新",
                                command=(lambda: _thread.start_new_thread(update_files, tuple())))
    file_update_button.pack()

    # TODO:删除还没做
    create_dir_button = Button(files_frame, text="新建目录", command=create_dir)
    create_dir_button.pack()

    create_file_button = Button(files_frame, text="新建文件", command=create_file)
    create_file_button.pack()

    delete_button = Button(files_frame, text="删除", command=delete_action, bootstyle=(DANGER,))
    delete_button.pack()

    open_button = Button(files_frame, text="打开", command=open_file)
    open_button.pack()

    files_dig.lb1.bind("<Double-Button-1>", open_file)

    _thread.start_new_thread(update_files, ())

    files_frame.pack(side=LEFT)

    f = Frame(window)
    modified_ttkbootstrap.Button(f, text="运行程序", command=yx, bootstyle=SUCCESS).pack()
    modified_ttkbootstrap.Button(f, text="保存代码", command=bc, bootstyle=INFO).pack()
    modified_ttkbootstrap.Button(f, text="库管理", command=kgl, bootstyle=WARNING).pack()
    modified_ttkbootstrap.Button(f, text="放点音乐", command=yy, bootstyle=DANGER).pack()
    modified_ttkbootstrap.Button(f, text="代码提示", command=dmts, bootstyle=DARK).pack()

    f.pack(side=RIGHT)
    editor_tab = notebookWithCloseBtn.CustomNotebook(tkinter.ttk, window)
    # editor_tab.sb()

    i = 'from time import *\n\n\n# 以下是示例代码\nprint("欢迎使用PyFactory 3.0！！！")\nsleep(5)\n'

    textbox, text, now, mc2 = editor.get_new_editor(editor_tab, mc2, window, title_obj, mode, zt, is_py, i)
    editor_tab.add(textbox, text=file_info[1])
    editor_tab.pack()
    now_editor = (textbox, text, now, mc2)

    window.f()
    window.protocol("WM_DELETE_WINDOW", close_window)
    window.mainloop()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


fileType = "NoFile"
''''''
print(is_admin())
if not is_admin():
    if sys.version_info[0] == 3:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        try:
            exit()
        except NameError:
            sys.exit()
    else:  # in python2.x
        exec("ctypes.windll.shell32.ShellExecuteW(None, u'runas', unicode(sys.executable), unicode(__file__), None, 1)")


def open_url():
    webbrowser.open("http://wry.ljcsunrise.tech/wp/index.php/")


def open_url1():
    webbrowser.open("http://wry.free.svipss.top/index.php?action=page.index")


def fuck():
    try:
        dqwj()
    except Exception:
        messagebox.showerror("出错了！",
                             "错误代码：" + traceback.format_exc() + "，请联系开发团队wry_beiyong07@outlook.com！")


class SettingsDlg(ModalWindow):
    """设置窗口"""

    class UpdateDlg(ModalWindow):
        """更新窗口"""

        def __init__(self):
            """初始化"""
            ModalWindow.__init__(self, m=settings)

            self.title("PyFactory产品更新")

            self.lbl1 = Label(self, text="检查：")
            self.lbl1.pack()
            self.pbar1 = Progressbar(self, length=100 * 3)
            self.pbar1.pack()
            self.lbl2 = Label(self, text="下载：")
            self.lbl2.pack()
            self.pbar2 = Progressbar(self, length=100 * 3)
            self.pbar2.pack()

            self.g1 = Frame(self)
            self.b1 = modified_ttkbootstrap.Button(self.g1, text="死剁噗！", bootstyle=(DANGER,), command=None)
            self.b1.pack(side=LEFT)
            self.b2 = ttk.Button(self.g1, text="FUCK OFF！！！",
                                 command=(lambda: (
                                     self.withdraw(), self.m.attributes("-disable", False), self.m.focus_force())))
            self.b2.pack(side=RIGHT)
            self.g1.pack()

            self.gx = Label(self, text="无法检查更新，更新服务器已经废了", font=("", 25))

            self.stat = tkinter_stat.StatusBar(self, status="无法检查更新，更新服务器已经废了")
            self.stat.display()
            self.pbar1.config(maximum=100)
            # _thread.start_new_thread(self.check, tuple())

        def check(self):
            """检查更新"""
            try:
                self.pbar2.config(value=0)
                v = requests.get("http://wry.ljcsunrise.tech/projects/pyfactory/latest.txt")
                self.pbar1.config(value=50)
                ver = v.text
                self.pbar1.config(value=100)
                if float(ver) > float(VERSION):
                    self.stat.config(status="发现更新，正在下载...")
                    dkwy("http://wry.ljcsunrise.tech/projects/pyfactory/latest_download")
                    self.pbar2.config(value=100)
                    self.stat.config(status="刚从浏览器下载一个更新，请查看浏览器下载项目。")
                else:
                    self.stat.config(status="无可用更新")
            except Exception:
                tkinter.messagebox.showerror("出现错误", traceback.format_exc())
                self.stat.config(status="出现错误")

    def __init__(self):
        super(SettingsDlg, self).__init__(m=zck)
        self.update_win = None
        self.selector = None
        self.title("设置 - PyFactory3.0")

        self.space0 = Label(self, text="")
        self.space0.pack()
        self.grp1 = LabelFrame(self, text="版本")

        '''self.group_label1 = Label(self, text="版本")

        self.group_label1.place(x=10, y=10)'''

        self.space1 = Label(self.grp1, text="")
        self.space1.pack()
        self.grid1 = Frame(self.grp1)
        self.space2 = Label(self.grid1, text=" ")
        self.space2.grid(column=1, row=1)
        self.jcgx = ttk.Button(self.grid1, text="检查更新", command=self.update_, bootstyle=(OUTLINE, SUCCESS))
        self.jcgx.grid(row=1, column=2)
        self.version = Label(self.grp1, text=" 当前版本：" + str(VERSION))
        self.version.pack()

        # TODO 自动更新
        try:
            self.c1 = Checkbutton(self.grp1, text="允许自动更新")
            self.c1.pack()
            self.c1.invoke()
            self.tip = Label(self.grp1, text="请注意，无法自动更新")
            self.tip.pack()
        except Exception:  # shif
            messagebox.showerror("错误", traceback.format_exc())

        self.grid1.pack()
        self.space3 = Label(self.grp1)
        self.space3.pack()

        self.grp1.pack()

        self.witespace1 = Label(self, text='\n')
        self.witespace1.pack()

        self.grp2 = LabelFrame(self, text="外观和字体（暂不可用）")

        '''        self.group_label2 = Label(self, text="外观和字体")
       self.group_label2.place(x=11, y=200 - 20)'''

        self.grp2.w1 = Label(self.grp2, text=str())
        self.grp2.w1.pack()
        self.btnlst1 = []
        for i in ["代码字体", "代码颜色", "字体颜色"]:
            self.btnlst1 += [modified_ttkbootstrap.Button(self.grp2, text="更改" + i, bootstyle=OUTLINE)]
            self.btnlst1[-1].pack()
        self.grp2.w2 = Label(self.grp2, text=str())
        self.grp2.w2.pack()

        self.btnlst1[0].config(command=self.codeFont)

        self.grp2.pack()

    def codeFont(self):
        """代码字体"""
        try:
            self.attributes("-disable", True)
            self.selector = font_selector.Mystyle(val={
                "font": str(),
                "size": int(),
                "underline": bool(),
                "delete": bool(),
                "bold": bool(),
                "i": bool()
            })
            self.selector.focus_force()
            self.selector.title("代码字体选择")
            self.selector.wm_protocol("WM_DELETE_WINDOW",
                                      (lambda: (self.selector.withdraw(), self.attributes("-disable", False))))
        except Exception:
            messagebox.showerror('', str(traceback.format_exc()))

    def update_(self):
        """更新"""
        self.update_win = self.UpdateDlg()


def create_s():
    """创建设置窗口"""
    global settings
    settings = SettingsDlg()


class StartWindow(QtWidgets.QMainWindow, StartUI):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)


def main():
    global zck, app, myWindow
    app = QtWidgets.QApplication(sys.argv)
    myWindow = StartWindow()
    myWindow.show()

    # 主窗口
    zck = Tk()
    zck.title("PyFactory3.0")
    zck.geometry("325x380")

    Label(zck, text="PyFactory 3.0", font=("kaiti", 20)).pack()
    Label(zck, text="一个轻便的Python编译器").pack()
    Label(zck, text="制作团队：若宇工作室").pack()
    Label(zck, text="请确保此电脑已安装Python").pack()
    label_link = Button(zck, text="官网：http://wry.ljcsunrise.tech/wp/", cursor="hand2",
                        command=open_url, bootstyle=(LINK, PRIMARY))
    label_link.pack()
    label_link1 = Button(zck, text="交流：http://wry.free.svipss.top/", cursor="hand2",
                         command=open_url1, bootstyle=(LINK, PRIMARY))
    label_link1.pack()

    zck.iconbitmap("icon.ico")
    Button(zck, text="新建文件", command=xjwj, bootstyle=(INFO, OUTLINE)).pack()
    Button(zck, text="读取文件", command=fuck, bootstyle=(WARNING, OUTLINE)).pack()
    Button(zck, text="库管理", command=kgl, bootstyle=(DANGER, OUTLINE)).pack()
    Button(zck, text="背景音乐", command=yy, bootstyle=(PRIMARY, OUTLINE)).pack()
    Button(zck, text="代码词典", command=dmts, bootstyle=(SUCCESS, OUTLINE)).pack()
    Button(zck, text="设置", command=create_s, bootstyle=(DARK, OUTLINE)).pack()
    Button(zck, text="关于", command=info, bootstyle=(INFO, OUTLINE)).pack()
    myWindow.close()
    zck.mainloop()


def info():
    w = Toplevel()
    w.title("关于")
    H1 = Label(w, text="关于Pyfactory", font=['', 20])
    H1.pack()
    v = Label(w, text="版本：" + str(VERSION))
    v.pack()
    p = Label(w, text="制作团队：王若宇（功能设计）、于泽（框架）、刘镕硕（实现）")
    p.pack()
    k = Label(w, text="版权所有，盗版必究")
    k.pack()
    py = Label(w, text="使用Python以及ttkbootstrap制作")
    py.pack()
    fgggg = LabelFrame(w, text="联系我们")
    f1 = Label(fgggg, text="电话：130 4984 2481")
    f1.pack()
    f2 = Button(fgggg, text="邮箱：wry_beiyong06@outlook.com", bootstyle=(LINK, PRIMARY), cursor="hand2",
                command=(lambda: webbrowser.open("mailto://wry_beiyong06@outlook.com")))
    f2.pack()
    f3 = Label(fgggg, text="QQ：2148505950")
    f3.pack()
    fgggg.pack()
    w.focus_force()


main()
