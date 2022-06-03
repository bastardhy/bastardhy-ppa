from tkinter import *
import tkinter.ttk
import time   #import library class time untuk menampilkan jam dalam kondisi real time
 
#membuat form registrasi
class registrasi:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol('WM_DELETE_WINDOW', self.close)
        self.parent.geometry('700x600')
        self.parent.resizable(False,False)
 
        self.setjam = StringVar()  # dikonersi ke dalam nilai string
        self.label = StringVar()  #nilai jam di jadikan kedalam label nilai string
         #self.close();
        #self.opendir()
        self.pengaturan()
        self.times()
        self.panjang = 30
 
    def pengaturan(self):
        mainform = Frame(self.parent)
        mainform.pack(fill=BOTH, expand=YES)
 
        #pendefinisian jam kedalam label (posisi) jam
        self.jamlbl = Label(mainform, textvariable=self.setjam, font='Helvetica')
        self.jamlbl.grid(row=0, column=3)
        #self.jamlbl.pack(expand=YES)
 
        #membuat label
        Label(mainform, text='Nama Mahasiswa').grid(row=1, column=0, padx=25, sticky=W)
        Label(mainform, text='NIM Mahasiswa').grid(row=2, column=0, padx=25, sticky=W)
        Label(mainform, text='Program Study   ').grid(row=3, column=0, padx=25, sticky=W)
        Label(mainform, text='Jenis Kelamin').grid(row=4, column=0, padx=25, sticky=W)
 
#membuat textfield
        self.namaMhs = Entry(mainform)
        self.nimMhs = Entry(mainform)
        self.namaMhs.grid(row=1, column=1, sticky=W)
        self.nimMhs.grid(row=2, column=1, sticky=W)
 
#membuat setfokus kursor pada textfield nama mahasiswa
self.namaMhs.focus_set()
 
#membuat combo box
self.jur = ('Teknik Informatika','Sistem Informatika')
self.jurusan = tkinter.ttk.Combobox(mainform, values=self.jur, width=17)
self.jurusan.grid(row=3, column=1, sticky=W)
 
        #membuat radiobutton
        self.radio = StringVar()
        self.radiobutton = tkinter.ttk.Radiobutton(mainform, variable=self.radio, text='Laki-laki', value=1, width=23)
        self.radbut = tkinter.ttk.Radiobutton(mainform, variable=self.radio, text='Perempuan', value=2)
        self.radiobutton.grid(row=4, column=1, sticky=W)
        self.radbut.grid(row=4, column=1, sticky=E)
 
    #pendefinisian jam
    def times(self):
        self.jam = time.strftime("%H:%M:%S", time.localtime())
        self.setjam.set(self.jam)
        self.timer = self.parent.after(1000,self.times)
#close windows
    def close(self, event=None):
        self.parent.destroy()
 
if __name__ == '__main__':
    main = Tk()
    registrasimahasiswa = registrasi(main, "form registrasi")
    main.mainloop()