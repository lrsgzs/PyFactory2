import _tkinter

try:
    import Tkinter as tk
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    from tkinter import ttk
from tkinter import messagebox


class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, oldtk, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True
        self.sb = self.__initialize_custom_style

        kwargs["style"] = "CustomNotebook"
        oldtk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        if messagebox.askokcancel("确认关闭？", "关闭窗口将可能丢失未保存的数据！"):
            pass
        else:
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        try:
            style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"), border=8, sticky='')
            style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
            style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                            })
                        ]
                    })
                ]
            })

        ])
        except _tkinter.TclError:
            pass


if __name__ == "__main__":
    root = tk.Tk()

    notebook = CustomNotebook(width=200, height=200)
    notebook.pack(side="top", fill="both", expand=True)

    for color in ("red", "orange", "green", "blue", "violet"):
        frame = tk.Frame(notebook, background=color)
        notebook.add(frame, text=color)

    root.mainloop()
'''
这是在Linux系统上的样子：

enter image description here
 相关讨论
使每个选项卡的新元素唯一有多困难？在我的应用程序中，我需要一个"关闭"元素和一个"保存/修改"元素，当当前未保存或保存内容时，它会变成红色或灰色(就像在Notepad ++中一样)。我面临的问题是如何控制每个选项卡中的"保存"元素颜色。因此，在这里为您提供答案，当您单击"关闭"元素时，如何使一个"关闭"元素改变颜色？ (当然，不是关闭选项卡/子项)
好的，我刚刚找到了stackoverflow.com/questions/23038356/，它在谈论主题而不是样式。仍在尝试消化它...当然，该示例并未解决您的其他元素的额外复杂性...
很棒的例子！您能解释一下tk.PhotoImage中数据的来源吗？我尝试自己进行搜索，但是所有其他代码示例似乎都使用了本地图像(扩展名为.png，.gif)
是否可以修改此代码，以便仅当鼠标光标悬停在选项卡中的x元素上时，选项卡中的x按钮才将颜色更改为红色或黄色？这样，用户就不会在偶然选择和关闭选项卡之间混淆。
我非常喜欢使用此代码，谢谢！！！
修复了通过将构造函数修改为以下内容来创建多个笔记本的错误：

1
2
3
4
    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            CustomNotebook.__initialized = True
希望其他人也可以利用：-)

 相关讨论
很高兴你喜欢。
'''
