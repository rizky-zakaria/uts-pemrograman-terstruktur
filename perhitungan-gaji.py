import string
print("Copyright By @rizkyzakaria_")
kdKaryawan = input("Masukan Kode Karyawan: ")
namaKaryawan = input("Masukan Nama Karyawan: ")
golongan = input("Masukan Golongan: ")
a = 10000000
b = 8500000
c = 7000000
d = 5500000
gp = 0
if(golongan == "A"):
    gp = a
elif(golongan == "B"):
    gp = b
elif(golongan == "C"):
    gp = c
elif(golongan == "D"):
    gp = d
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")


if(golongan == "A"):
    p = 1000000 * 2.5 / 100
elif(golongan == "B"):
    p = 8500000 * 2 / 100
elif(golongan == "C"):
    p = 7000000 * int(1.5) / 100
elif(golongan == "D"):
    p = 5500000 * 1 / 100
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")


if(golongan == "A"):
    gb = str(int(1000000-1000000*2.5/100))
elif(golongan == "B"):
    gb = str(int(8500000-8500000*2/100))
elif(golongan == "C"):
    gb = str(int(7000000-7000000*1.5/100))
elif(golongan == "D"):
    gb = str(int(5500000-5500000*1/100))
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")

print("==========================================")
print("       STRUK RINCIAN GAJI KARYAWAN        ")
print("..........................................")
print("Nama Karyawan : " + namaKaryawan + "   Kode: " + kdKaryawan)
print("Golongan : " + golongan)
print("..........................................")
print("Gaji Pokok : Rp." + str(gp))
print("Potongan 1% : " + str(int(p)))
print("..........................................")
print("Gaji Bersih : " + gb)
