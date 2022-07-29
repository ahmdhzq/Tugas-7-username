# Nama  : Ahmad Haziq Mu'izzaddin Wafiq
# Kelas : Pengembangan Perangkat Lunak(PPL)

import os
os.system('cls')

status = ''


def username():
    print()
    inputan = input("Masukkan Username : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3 = inputan.capitalize()

    if cek1 > 9 and cek2 == False and cek3 == inputan:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Username tidak valid"
        status = "Gagal"
        return inputan, status


def email():
    print()
    inputan = input("Masukkan Email : ")
    cek1 = len(inputan)
    cek2 = ' ' in inputan
    cek3= '@' and '.' in inputan

    if cek1 > 7 and cek2 == False and cek3 == True:
        status = "Berhasil"
        return inputan, status

    else:
        inputan = "Email tidak valid"
        status = "Gagal"
        return inputan, status


def phone():
    print()
    inputan = str(input("Masukkan Phone : "))
    cek1 = len(inputan)
    cek2 = ' ' in inputan

    if cek1 < 13 and cek2 == False:
        status = "Berhasil"
        return inputan, status
    else:
        inputan = "Phone tidak valid"
        status = "Gagal"
        return inputan, status


def main():
    while True:
        u1, u2 = username()
        print("=" * 40)
        print("Username = ", u1)
        print("Status = ", u2)
        print("=" * 40)
        if u2 == "Berhasil":
            break

    while True : 
        e1, e2 = email()
        print("-" * 40)
        print("\nEmail = ", e1)
        print("Status = ", e2)
        print("-" * 40)
        if e2 == "Berhasil":
            break

    while True : 
        p1, p2 = phone()
        print("+" * 40)
        print("\nPhone = ", p1)
        print("Status = ", p2)
        print("+" * 40)
        if p2 == "Berhasil":
            break
   

main()