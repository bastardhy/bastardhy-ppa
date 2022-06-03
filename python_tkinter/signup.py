
from tkinter import *

root = Tk()

username = Label(root, text='firstname :')
password = Label(root, text='lastname :')
userbox = Entry(root)
passbox = Entry(root)

signin = Button(root, text='Sign In')
signup = Button(root, text='Sign Up')

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="lokalisasi", db="python")

cur = db.cursor()

sql = "INSERT INTO name(firstname, lastname) VALUES"
cur.execute(sql)


username.grid(row=0, column=0)
password.grid(row=1, column=0)
userbox.grid(row=0, column=1)
passbox.grid(row=1, column=1)

#Kita bungkus tombolnya di kanan bawah
signin.grid(row=2, column=2)
signup.grid(row=2, column=3)

root.mainloop()