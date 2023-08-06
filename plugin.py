import tkinter
import modified_ttkbootstrap
import pickle
import os


class ScrollListbox(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.scr1 = modified_ttkbootstrap.Scrollbar(self)
        self.scr2 = modified_ttkbootstrap.Scrollbar(self, orient=tkinter.HORIZONTAL)
        self.scr1.pack(side=tkinter.RIGHT, fill="y")
        self.scr2.pack(side=tkinter.BOTTOM, fill="x")

        self.lb1 = tkinter.Listbox(self, yscrollcommand=self.scr1.set, xscrollcommand=self.scr2.set)
        self.lb1.pack(side=tkinter.LEFT, fill="both")

        self.scr1.config(command=self.lb1.yview)
        self.scr2.config(command=self.lb1.xview)


class SetupHelper(object):
    def __init__(self, file):
        self.file_name = file

        try:
            file = open(self.file_name, "rb")
        except:
            file = open(self.file_name, "wb")
            pickle.dump({}, file)
            file.close()
            file = open(self.file_name, "rb")

        self.setup_dict: dict = pickle.load(file)
        file.close()

    def save_file(self):
        file = open(self.file_name, "wb")
        pickle.dump(self.setup_dict)
        file.close()

    def save_item(self, name, obj):
        self.setup_dict[name] = obj

    def get_item(self, name):
        item = self.setup_dict[name]
        return item

    def get_all_item(self):
        items = self.setup_dict.copy()
        return items


class TitleObject:
    def __init__(self, title_=""):
        self.title_ = title_


def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    path = path.rstrip("/")
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        return True
    else:
        return False


def mkfile(name):
    try:
        temp = open(name, "rb")
        temp.close()
        return False
    except:
        temp = open(name, "w")
        temp.close()
        return True
