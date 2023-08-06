from threading import RLock, Thread
from tkinter import Canvas, Text


class LineNumber(object):
    def __init__(self, window, text, frm):
        self.txt = ''
        self.thread_lock = RLock()
        self.text = text
        self.window = window
        self.edit_frame = frm
        self.edit_frame.pack()
        self.line_text = Text(self.edit_frame, width=7, height=600, spacing3=5,
                              bg="#DCDCDC", bd=0, font=('Hack', 14), takefocus=0, state="disabled",
                              cursor="arrow")
        self.line_text.pack(side="left", expand=True)
        self.window.update()

    def wheel(self, event):
        self.line_text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        self.text.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    def scroll(self, *xy):
        self.line_text.yview(*xy)
        self.text.yview(*xy)

    def get_txt_thread(self):
        Thread(target=self.get_txt).start()

    def get_txt(self):
        self.thread_lock.acquire()
        if self.txt != self.text.get("1.0", "end")[:-1]:
            self.txt = self.text.get("1.0", "end")[:-1]
            self.show_line()
        else:
            self.thread_lock.release()

    def show_line(self):
        sb_pos = self.text.vbar.get()
        self.line_text.configure(state="normal")
        self.line_text.delete("1.0", "end")
        txt_arr = self.txt.split("\n")
        if len(txt_arr) == 1:
            self.line_text.insert("1.1", " 1")
        else:
            for i in range(1, len(txt_arr) + 1):
                self.line_text.insert("end", " " + str(i))
                if i != len(txt_arr):
                    self.line_text.insert("end", "\n")
        if len(sb_pos) == 4:
            self.line_text.yview_moveto(0.0)
        elif len(sb_pos) == 2:
            self.line_text.yview_moveto(sb_pos[0])
            self.text.yview_moveto(sb_pos[0])
        self.line_text.configure(state="disabled")
        try:
            self.thread_lock.release()
        except RuntimeError:
            pass
