

firstname = input("Nama Depan: ")
lastname = input("Nama Belakang: ")

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="lokalisasi", db="python")

cur = db.cursor()

siswa = (firstname, lastname)
sql = "INSERT INTO name(firstname, lastname) VALUES"+str(siswa)
cur.execute(sql)



cur.close()
db.commit()
db.close()