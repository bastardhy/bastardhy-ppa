from tkinter import *

root = Tk()

header = Frame(root, bg='red', width= 800, height=30)
header.pack(side=TOP, fill=X)
footer = Frame(root, bg='blue', width=500, height=20)
footer.pack(side=BOTTOM, fill=X)

root.mainloop()