from tkinter import *

root = Tk()

Label(root,
   text="Teks ini menggunakan jenis font 'Times' ",
   font = "Times").pack()
Label(root,
   text="Teks ini menggunakan font 'Helvetica' dengan style 'italic' ukuran 16",
   font = "Helvetica 16 bold italic").pack()
Label(root,
   text="Teks ini menggunakan font 'Verdana' dengan ukuran '10' dan style 'bold' ",
   font = "Verdana 10 bold").pack()

root.mainloop()