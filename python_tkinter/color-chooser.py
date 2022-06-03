from tkinter import Tk, Frame, Button, BOTH, SUNKEN, colorchooser

class pemilihWarna(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("pemilih warna")
        self.window.geometry("800x150")
        self.pack(fill=BOTH, expand=1)

        self.buatTombol()
        self.buatTempatWarna()

    def buatTombol(self):
        self.tombol = Button(self, text="pilih warna", command=self.pilihWarna)
        self.tombol.place(x=30, y=30)

    def buatTempatWarna(self):
        self.tempatWarna = Frame(self, border=1,relief=SUNKEN, width=100, height=100)
        self.tempatWarna.place(x=160, y=30)

    def pilihWarna(self):
        (rgb, hx) = colorchooser.askcolor()
        self.tempatWarna.config(bg=hx)

if __name__ == '__main__':
    root = Tk()
    ex = pemilihWarna(root)
    root.mainloop()
