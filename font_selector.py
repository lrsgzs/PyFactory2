import builtins
import ntpath
import tkinter as tk
from tkinter import ttk, font


# from configparser import ConfigParser
import modified_ttkbootstrap
from modified_ttkbootstrap import DANGER


class Mystyle(tk.Toplevel):
    def __init__(self, master=None, file="codefont.ryconfigs", val='', *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        if not ntpath.exists(file):
            with builtins.open(file, "w+") as f:
                f.write(str(val))
            f.close()

        self.family = tk.StringVar(value=font.names()[0])
        self.fontsize = tk.StringVar(value="10")
        self.underline = tk.IntVar()
        self.overstrike = tk.IntVar()
        self.weight = tk.StringVar(value="normal")
        self.slant = tk.StringVar(value="roman")
        self.defaultfont = {"family": font.names()[0], "size": "10", "weight": "normal", "slant": 'roman',
                            "underline": 0, "overstrike": 0}
        self.fontdict = self.defaultfont.copy()
        self.varsdict = {"family": self.family, "size": self.fontsize, "weight": self.weight, "slant": self.slant,
                         "underline": self.underline, "overstrike": self.overstrike}
        self.style = ttk.Style()
        self.creatwidget()

    def creatwidget(self):

        self.style.configure("TLabelframe", background="white", relief="groove")
        self.style.configure("TFrame", background="white", )

        lf = ttk.LabelFrame(self, text="字体设置", labelanchor='n')
        lf.pack(side='top', expand=1, fill="both", padx=10, pady=10)

        # 字体选择部分
        lfl = ttk.LabelFrame(lf, text="字体", labelanchor='n')
        lfl.pack(side='left', expand=1, fill="both", padx=5, pady=5)
        fontsfam = sorted([i for i in font.families() if not i.startswith("@")], reverse=True)
        fambox = self.enlistbox(lfl, self.family, fontsfam)
        # 字号选择部分
        lfr = ttk.LabelFrame(lf, text="字号", labelanchor='n')
        lfr.pack(side='left', expand=1, fill="both", padx=5, pady=5)
        sizebox = self.enlistbox(lfr, self.fontsize, [i for i in range(8, 80, 2)])

        lft = ttk.Frame(lf, )
        lft.pack(side='left', expand=1, fill="both", padx=5, pady=5)
        # 复选框部分
        self.special(lft)

        # 样式预览部分
        self.lf2 = ttk.LabelFrame(lft, text="样式预览", labelanchor='n')
        self.lf2.pack(side='top', expand=1, fill="both", padx=5, pady=5)
        self.example(self.lf2, self.defaultfont)
        self.setdefault()
        # 按钮部分
        lfbottom = tk.Frame(self, )
        lfbottom.pack(side="top", expand=0, fill="x", padx=10, pady=10)
        modified_ttkbootstrap.Button(lfbottom, text="恢复默认", command=self.setdefault,bootstyle=(DANGER,)).pack(side="right", padx=5, pady=5)
        ttk.Button(lfbottom, text="确定", command=self.setfont).pack(side='right', padx=5, pady=5)

    # 建立输入框和选择列表组合,供选择自体和字号
    def enlistbox(self, parent, somevar, listvar, ):
        def editfontsize(event):
            var = event.widget.curselection()
            if var:
                fam = event.widget.get(var)
                if str(fam).isdigit():
                    self.fontsize.set(fam)
                else:
                    self.family.set(fam)
            self.update_font()

        en = ttk.Entry(parent, textvariable=somevar)
        en.pack(side="top", expand=0, fill="x", padx=5, )
        lib = tk.Listbox(parent, selectmode="single")
        lib.pack(side="top", expand=1, fill="both", padx=5, )
        sc = tk.Scrollbar(lib)
        sc.pack(side="right", expand=0, fill="y")
        lib.yview_scroll = sc.set
        lib.insert("end", *listvar)
        somevar.set(listvar[0])
        lib.bind("<<ListboxSelect>>", editfontsize)
        return lib

    # 界面字体更新的示例
    def example(self, parent, fontdict):
        for i in parent.winfo_children():
            i.destroy()
        tex = ttk.Label(parent, text="print('Hello World!')\ninput('你好，世界！')", )
        tex.pack(expand=1, fill="both", padx=15, pady=15)
        tex.configure(font=font.Font(**fontdict))

    # 复选框部分
    def special(self, parent):
        lf1 = ttk.LabelFrame(parent, text="特殊效果", labelanchor='n')
        lf1.pack(side='top', expand=0, fill="x", padx=5, pady=5)
        tempdict = [
            dict(text="下划线", variable=self.underline, offvalue=0, onvalue=1, command=self.update_font, bg="white"),
            dict(text="删除线", variable=self.overstrike, offvalue=0, onvalue=1, command=self.update_font, bg="white"),
            dict(text="加粗", variable=self.weight, offvalue="normal", onvalue="bold", command=self.update_font,
                 bg="white"),
            dict(text="斜体", variable=self.slant, offvalue="roman", onvalue="italic", command=self.update_font,
                 bg="white"),
        ]
        for i in tempdict:
            c1 = tk.Checkbutton(lf1, **i)
            c1.pack(side="left", padx=10, pady=10)

    # 更新自体存储字典
    def update_font(self):
        for i, k in self.varsdict.items():
            self.fontdict[i] = k.get()
        self.example(self.lf2, self.fontdict)

    # 设置所有字体变化,确定按钮
    def setfont(self):
        self.update_font()
        for i in font.names():
            print(i)  # font.Font(name=i, exists=True, **self.fontdict)
        self.toFile()
        self.destroy()

    def toFile(self):
        """应用到文件"""

    # 设置所有自体初始化,取消按钮
    def setdefault(self):
        for i, k in self.varsdict.items():
            k.set(self.defaultfont[i])
        self.example(self.lf2, self.defaultfont)
        for i in font.names():
            pass  # font.Font(name=i, exists=True, **self.defaultfont)
        # self.destroy()

    def editcolor(self, event):
        pass

        # co=colorchooser.askcolor()[1]
        # print(event.widget._name)
        # codict={event.widget._name:co}
        # self.style.configure("TLabel",**codict)


if __name__ == "__main__":
    # root  = tk.Tk()
    # # root.option_add("*Font", "微软雅黑")
    # # root.iconbitmap('crown.ico')
    root = Mystyle()
    root.title("DATA")
    root.attributes("-alpha", 1)  # 设置透明度用的，最大值是1不透明
    root.geometry("{}x{}+{}+{}".format(root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2,
                                       root.winfo_screenwidth() // 4, root.winfo_screenheight() // 4))
    root.mainloop()
