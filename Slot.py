#HANYA EXAMPLE
#--------------------------------------------#
print("Selamat datang di slot game mesin!")
#--------------------------------------------#
numOfPlay = ('Berapa anda ingin bermain?')
gamePosisi = ["bar","bar","bar","cherry","crown"]
Kalah = ["/nAnda Kalah!"]
Uang = int(input ('Berapa banyak uang yang anda ingin mainkan?')
Perpullmoney = int(input ('Berapa banyak yang ingin Anda pertaruhkan per tarikan?')
#--------------------------------------------#                  
# Bagian ini membangun serangkaian kemungkinan jawaban.
# (disebut juga "elemen" dari array.
# Anda dapat mencoba menambahkan atau menghapus sesuatu ke daftar ini.
#--------------------------------------------#                 
from random import *
#--------------------------------------------#
# Bagian ini dimuat secara acak sehingga kita dapat menggunakan pilihan nanti.
# Impor adalah bagian Python yang sangat rapi, dan kami akan
# berbicara lebih banyak tentang mereka nanti, tetapi untuk saat ini, ketahuilah itu
# kita mendapatkan semua hal yang dimiliki secara acak.
# (itulah yang dilakukan tanda bintang, mengambil semua hal.)
#--------------------------------------------#
def play(currentmoney,Perpullmoney):
    slot1=choice(gamePosisi)
    slot2=choice(gamePosisi)
    slot3=choice(gamePosisi)
    sassyLoss = choice(Kalah)
    win = sassyLoss
#--------------------------------------------#
# Di sini kami menyiapkan tiga slot dengan menamai tiga variabel sebagai
# slot1, slot2, dan slot3. Jika kami menginginkan lebih, kami akan melakukannya
# membutuhkan slot4, slot5, dan sebagainya.
#
# fungsi choice () adalah dari acak yang kita impor
# di atas dan fungsi itu akan mendapatkan satu (dan hanya satu) dari
# elemen yang mungkin pada larik yang kita buat di atas.
#--------------------------------------------#
    if (slot1==slot2==slot3=="cherry"):
        win = "\nAnda menang "+str(Perpullmoney)
        currentmoney = currentmoney + int(Perpullmoney*10)
    if (slot1==slot2==slot3=="crown"):
        win = "\nAnda menang $50"
        currentmoney = currentmoney + int(50)
    if (slot1==slot2==slot3=="bar"):
        win = "\nAnda menang! $5"
        currentmoney = currentmoney + int(5)
    print(slot1+":"+slot2+":"+slot3+" "+win)
    return currentmoney
#--------------------------------------------#
# Di sinilah kami memutuskan apakah Anda menang. Kami memeriksa untuk melihat
# jika ketiga variabel slot semuanya ekuivalen (ingat
# yang Anda inginkan equilivant (==) bukan tugas (=).
# saat semuanya sama dan cocok dengan string terakhir, maka
# kita melakukan sesuatu dengannya. Dalam hal ini, kami mengembalikannya untuk dicetak. 
#--------------------------------------------#
for i in range(int(numOfPlay)):
    Uang = Uang - int(Perpullmoney)
    Uang = int(play(Uang, Perpullmoney))
    print("Kamu mempunyai "+str(Uang)+" left.")
                   
#kita harus menambahkan pelacak untuk kemenangan
