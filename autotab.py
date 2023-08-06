def enter():
    pass


class Taber:
    def __init__(self, window, text):
        self.root = window
        self.text = text
        self.text.bind("<Return>", self.enter)
        self.text.pack()

    def enter(self, *args):
        enter()
        self.i = 0
        a = self.text.index('insert')
        a = float(a)
        aa = int(a)
        b = self.text.get(float(aa), a).replace('\n', '')
        c = b
        if b[-1:] == ':':
            i = 0
            while True:
                if b[:4] == '    ':
                    b = b[4:]
                    i += 1
                else:
                    break
            self.i = i + 1
        else:
            i = 0
            while True:
                if b[:4] == '    ':
                    b = b[4:]
                    i += 1
                else:
                    break
            self.i = i
            if c.strip() == 'break' or c.strip() == 'return' or c.strip() == 'pass' or c.strip() == 'continue':
                self.i -= 1
        self.text.insert('insert', '\n')
        for j in range(self.i):
            self.text.insert('insert', '    ')
        return 'break'

    def run(self):
        self.root.mainloop()
