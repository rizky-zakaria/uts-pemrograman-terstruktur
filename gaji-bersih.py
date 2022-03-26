import string
print("Copyright By @rizkyzakaria_")
anak = 0
stm = ""
kdKaryawan = input("Masukan Kode Karyawan: ")
namaKaryawan = input("Masukan Nama Karyawan: ")
golongan = input("Masukan Golongan: ")
status = input("Masukan Status: 1 = Menikah / 2 = Belum : ")
if status == "1":
    stm = "Menikah"
    anak = int(input("Masukan Jumlah Anak: "))
elif status == "2":
    stm = "Belum Menikah"
else:
    print("Masukan Data Yang Valid!")

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
    persen = "2,5"
    p = gp * 2.5 / 100
elif(golongan == "B"):
    persen = "2"
    p = gp * 2 / 100
elif(golongan == "C"):
    persen = "1,5"
    p = gp * int(1.5) / 100
elif(golongan == "D"):
    persen = "1"
    p = gp * 1 / 100
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")


tis = 0
ta = 0
if status == "1":
    tis = gp*10/100
    ta = gp*5/100*anak

gk = 0
if(golongan == "A"):
    gk = int(gp + tis + ta)
elif(golongan == "B"):
    gk = int(gp + tis + ta)
elif(golongan == "C"):
    gk = int(gp + tis + ta)
elif(golongan == "D"):
    gk = int(gp + tis + ta)
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")

if(golongan == "A"):
    gb = str(int(gk - p))
elif(golongan == "B"):
    gb = str(int(gk - p))
elif(golongan == "C"):
    gb = str(int(gk - p))
elif(golongan == "D"):
    gb = str(int(gk - p))
else:
    print("Masukan Golongan Yang Valid : A/B/C/D")

print("==========================================")
print("       STRUK RINCIAN GAJI KARYAWAN        ")
print("..........................................")
print("Nama Karyawan : " + namaKaryawan + "   Kode: " + kdKaryawan)
print("Golongan : " + golongan)
print("Status Menikah : " + stm)
print("Jumlah Anak : " + str(anak))
print("..........................................")
print("Gaji Pokok : Rp." + str(gp))
print("Tunjangan Istri/Suami : Rp." + str(int(tis)))
print("Tunjangan Anak : Rp." + str(int(ta)))
print("......................................... +")
print("Gaji Kotor: " + str(int(gk)))
print("Potongan " + persen + "% : " + str(int(p)))
print("..........................................")
print("Gaji Bersih : " + gb)
