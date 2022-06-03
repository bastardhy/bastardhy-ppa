from tkinter import Tk, Frame, BOTH
class mengubahJudul(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background = "white")

        self.tampilan = parent

        self.initUI()

    def initUI(self):
        self.tampilan.title("ini judul nya")
        self.pack(fill=BOTH, expand=1)
        self.tampilan.geometry("250x150+300+300")

if __name__ == '__main__':
    root = Tk()
    app = mengubahJudul(root)
    root.mainloop()