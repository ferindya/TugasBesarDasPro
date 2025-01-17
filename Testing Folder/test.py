# Digunakan untuk mengetest command-command sebelum dimasukan kedalam file utama

'''
import time

    # Random Number untuk Kerang Ajaib
n = int(input("Panjang list:"))

local = time.localtime()
current = time.strftime("%S", local)
print(current)
year = time.strftime("%Y", local)       # Untuk tahunnya
print(year)

hasil = int(current) % n
print(hasil)
'''

# Padanan Standar ASCII
'''
print(ord('p')) # --> dari char -> ke angka
 
print(chr(112)) # --> dari angka --> char
'''

# Untuk konversi dari password asli ke password ciphered
'''
alphabet = "abcdefghijklmnopqrstuvwxyz"

password = "dahlah"
newpass = ""

for i in (password):
    if (i in alphabet or i in alphabet.upper()):
        code = ord(i)
        penambah = 29
        pengali = 4
        newcode = (code + 29)*4 
        codediv = newcode // 26
        codemod = newcode % 26
        newcodemod = codemod + 97
        newalp = chr(newcodemod)
        #print(newcode, codediv, codemod, newcodemod, newalp)
        newpass = newpass + str(codediv)+ newalp
    else:
        newpass = newpass + i

print(" ======================================= ")
# Fungsi penyimpanan --> y = chipered(x) = (ord(x) + kodepenambah) * kodepengali 
# Fungsi pembalik --> x = semula(y) = chr((y / kodepengali) - kodepenambah)
# String pemisah --> 907

print(newpass)
'''

'''
# Untuk ngubah dari password ciphered ke password asli
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newpass = "19k20u19k20q19o"

length = 0
for i in (newpass):
        length = length+1 

print(length)

finalcode = ""



i = 0
while (i < length):
    try:
        angka = int(newpass[i]+newpass[i+1])
        require1 = True
    except:
        angka = 0
        require1 = False
    
    if (require1 == True):
        if (i+2 < length and (newpass[i+2] in alphabet)):      #kalo alphabet, pasti huruf kecil
            code = newpass[i+2]
            require2 = True
        else:
            require1 = False
            require2 = False
        
    
    if(require1 == True and require2 == True):
        resultcode = (26*angka + ord(code) - 97 - 116)/4
        resultcode = chr(int(resultcode))
        i = i+3
    
    if(require1 == False):
        resultcode = newpass[i]
        i = i+1
    
    finalcode = finalcode + resultcode

print(finalcode)
'''

# Membuat fungsi dari csv menjadi list
'''
user = open("user.csv", "r")

# Ngukur panjang list
length = 0
for i in user:
    length +=1

# Lebar list 
# user --> 6, game --> 6, riwayat --> 5, kepemilikan --> 2

# lets say ini user data
datalist = [[0 for i in range (6)]for i in range (length)]
user.close()

user = open("user.csv", "r")
row = 0
for i in user:
    line = i
    col = 0
    word = ""
    for j in line:
        if (j == ";"):
            datalist[row][col] = word
            word = ""
            col +=1
        else:
            word = word + j
        
    row +=1

user.close()

for i in datalist:
    print(i)
'''

# Fungsi merge list
'''
list1 = [[1,2,3,4],
         [5,6,7,8]]
list2 = [9,1,2,3]

listinlist = [list2]
list3 = list1 + listinlist

print(list3)
'''

# Algoritma untuk memasukan list ke dalam csv
'''
from csvlistfunction import *

dataframe = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'],
                ['GAME001', 'Elden Ring', 'RPG', '2022', '600000', '5'],
                ['GAME002', 'Payday 2', 'FPS', '2013', '80000', '7'],
                ['GAME003', 'Outlast 2', 'Horror', '2017', '140000', '13']]

def listtocsv(file, component, folder, dataframe):
    if (file == 'user'):
        data = open("./csv files/"+folder+"/user.csv", "w")
    elif (file == 'game'):
        data = open("./csv files/"+folder+"/game.csv", "w")
    elif (file == 'riwayat'):
        data = open("./csv files/"+folder+"/riwayat.csv","w")
    elif (file == 'kepemilikan'):
        data = open("./csv files/"+folder+"/kepemilikan.csv", "w")

    length = lengthlist(dataframe)

    for row in range(length):
        line = ""
        for col in range(component):
            if (col == component - 1):
                line = line + dataframe[row][col] + "\n"
            else:
                line = line + dataframe[row][col]+";"
        
        # Masukkan setiap line kedalam csv
        data.write(line)
    
    data.close()

listtocsv('game', 6, 'main save', dataframe)
'''

# Membuat folder baru jika belum ada folder dengan nama tertentu
'''
import os
import time

print("Ketikkan '#time' bila ingin membuat folder sesuai waktu pelaksanaan save.")
folder = input()

# Jika pengguna menginput nama folder dengan "#time", maka nama yang diinputkan adalah waktu sebenarnya
local = time.localtime()                                # local adalah variabel untuk menyatakan localtime
timedata = time.strftime("%Y-%m-%d_%H%M%S", local)

if (folder == "#time"):
    folder = timedata

parent_dir = "./csv files"

path = os.path.join(parent_dir, folder)         # Fungsi untuk menggabung

os.mkdir(path)                                  # Command untuk membuat directory baru
'''
