from ast import If
print("Copyright By @rizkyzakaria_")

bhsIndo = int(input("Masukan Nilai Bahasa Indonesia: "))
ipa = int(input("Masukan Nilai IPA: "))
matematika = int(input("Masukan Nilai Matematika: "))

if bhsIndo > 100:
    print("Nilai Tidak Boleh Lebih Dari 100")
elif matematika > 100:
    print("Nilai Tidak Boleh Lebih Dari 100")
elif ipa > 100:
    print("Nilai Tidak Boleh Lebih Dari 100")
else:
    if bhsIndo < 60:
        print("Status Kelulusan : TIDAK LULUS!")
    elif matematika <= 70:
        print("Status Kelulusan : TIDAK LULUS!")
    elif ipa < 60:
        print("Status Kelulusan : TIDAK LULUS!")
    else:
        print("Status Kelulusan : LULUS!")
