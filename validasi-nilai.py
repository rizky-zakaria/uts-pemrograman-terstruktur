from ast import If
print("Copyright By @rizkyzakaria_")

bhsIndo = int(input("Masukan Nilai Bahasa Indonesia: "))
ipa = int(input("Masukan Nilai IPA: "))
matematika = int(input("Masukan Nilai Matematika: "))

if bhsIndo > 100:
    print("Maaf Input Ada Yang Tidak Valid")
elif matematika > 100 & matematika < 0:
    print("Maaf Input Ada Yang Tidak Valid")
elif ipa > 100 & ipa < 0:
    print("Maaf Input Ada Yang Tidak Valid")
else:
    if bhsIndo < 0:
        print("Maaf Input Ada Yang Tidak Valid")
    elif matematika < 70:
        print("Maaf Input Ada Yang Tidak Valid")
    elif ipa < 0:
        print("Maaf Input Ada Yang Tidak Valid")
    else:
        if bhsIndo < 60:
            print("Status Kelulusan : Anda Tidak Lulus!")
        elif matematika <= 70:
            print("Status Kelulusan : Anda Tidak Lulus!")
        elif ipa < 60:
            print("Status Kelulusan : Anda Tidak Lulus!")
        else:
            print("Status Kelulusan : Anda Lulus!")
