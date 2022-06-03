nama=input("Masukkan Nama Barang = ")
harga=int(input("Masukkan Harga Barang = "))
jumlah=int(input("Masukkan Jumlah Barang = "))
total=harga*jumlah
print("Total Pembelian Anda Adalah Rp.",total)
bayar=int(input("Uang Pembayaran = "))
hutang=total-bayar
if (bayar>total):
	print("Jumlah Kembalian",bayar-total)
else:
	print("Uang Anda Kurang Rp.",hutang)