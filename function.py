import random as rdm
from os import system

def clear():
    system("cls")

def memBil():

    # Membuat bilangan ratusan random
    bilangan = rdm.randrange(99, 1000)

    # Mengubah bilangan menjadi string
    bilStr = str(bilangan)

    # Membagi bilangan menjadi 3 bagian
    bil1 = int(bilStr[0])
    bil2 = int(bilStr[1])
    bil3 = int(bilStr[2])

    return bil1, bil2, bil3

def trueOrFalse(data, bil, digitBil):

    i = False

    if data == bil:
        clear()
        print("Digit bilangan", digitBil, "benar")
        i = True

    elif data > bil:
        print(data, "lebih besar daripada digit pertama\n\n")

    elif data < bil:
        print(data, "lebih kecil daripada digit pertama\n\n")

    else:
        print("Anda memasukkan format jawaban yang salah")

    if i == True:
        return True


def inputUser(blg, bil):
    
    cekBil = 0

    try:
        inputBil = int(input("Masukkan tebakan bilangan " + blg + " : "))

    except:
        print("Anda memasukkan format jawaban yang salah")

    else:
        cekBil = trueOrFalse(inputBil, bil, blg)
    
    if cekBil == True:
        return True



