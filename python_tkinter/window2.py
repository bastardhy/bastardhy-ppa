from tkinter import Tk, Frame
class mengubahJudul(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent,)

        self.tampilan = parent

        self.initUI()

    def initUI(self):
        self.tampilan.title("ini judul nya")


if __name__ == '__main__':
    root = Tk()
    app = mengubahJudul(root)
    root.mainloop()
