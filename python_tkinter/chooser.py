from tkinter import *

root = Tk()
root["bg"] = "grey"

Label(root,
   text="Teks ini menggunakan jenis font 'Times' ",
   fg = "red",
     bg = "yellow",
   font = "Times").pack()
Label(root,
   text="Teks ini menggunakan font 'Helvetica' dengan style 'italic' ukuran 16",
   fg = "dark green",
     bg = "light green",
   font = "Helvetica 16 bold italic").pack()
Label(root,
   text="Teks ini menggunakan font 'Verdana' dengan ukuran '10' dan style 'bold' ",
   fg = "blue",
     bg = "light blue",
   font = "Verdana 10 bold").pack()

root.mainloop()