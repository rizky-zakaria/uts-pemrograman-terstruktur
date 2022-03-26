from ast import If
print("Copyright By @rizkyzakaria_")

bhsIndo = int(input("Masukan Nilai Bahasa Indonesia: "))
ipa = int(input("Masukan Nilai IPA: "))
matematika = int(input("Masukan Nilai Matematika: "))

if bhsIndo > 100:
    print("Maaf Input Ada Yang Tidak Valid")
elif matematika > 100:
    print("Maaf Input Ada Yang Tidak Valid")
elif ipa > 100:
    print("Maaf Input Ada Yang Tidak Valid")
else:
    if bhsIndo < 0:
        print("Maaf Input Ada Yang Tidak Valid")
    elif matematika < 0:
        print("Maaf Input Ada Yang Tidak Valid")
    elif ipa < 0:
        print("Maaf Input Ada Yang Tidak Valid")
    else:
        if bhsIndo < 60:
            if matematika <= 70:
                if ipa < 60:
                    print("Status Kelulusan : Anda Tidak Lulus!")
                    print("Nilai Bahasa Indonesia Kurang Dari 60")
                    print("Nilai Matematika Kurang Dari 70")
                    print("Nilai Ipa Kurang Dari 60")
        elif bhsIndo < 60:
            if matematika <= 70:
                print("Status Kelulusan : Anda Tidak Lulus!")
                print("Nilai Bahasa Indonesia Kurang Dari 60")
                print("Nilai Matematika Kurang Dari 70")
        elif bhsIndo < 60:
            if ipa < 60:
                print("Status Kelulusan : Anda Tidak Lulus!")
                print("Nilai Bahasa Indonesia Kurang Dari 60")
                print("Nilai Ipa Kurang Dari 60")
        elif ipa < 60:
            if matematika <= 70:
                print("Status Kelulusan : Anda Tidak Lulus!")
                print("Nilai Ipa Kurang Dari 60")
                print("Nilai Matematika Kurang Dari 70")
        elif bhsIndo < 60:
            print("Status Kelulusan : Anda Tidak Lulus!")
            print("Nilai Bahasa Indonesia Kurang Dari 60")
        elif matematika <= 70:
            print("Status Kelulusan : Anda Tidak Lulus!")
            print("Nilai Matematika Kurang Dari 70")
        elif ipa < 60:
            print("Status Kelulusan : Anda Tidak Lulus!")
            print("Nilai Ipa Kurang Dari 60")
        else:
            print("Status Kelulusan : Anda Lulus!")
