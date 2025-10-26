"""
Nama Program: Lift 

Nama/NIM Anggota Kelompok:
Khasya Nurul Amini/19625007
Kezia Josephine Manik/19625015
Raya Medina Farrelin/19625183
Edward Terrance Lie/19625187

Deskripsi:
Program cara kerja lift. Terdapat 15 lantai, penamaan masing-masing lantai dapat diilihat dalam kamus. Untuk urutan lantai kelipatan 3n+1, pintu bagian depan terbuka.
Ketika program pertama kali dimulai, user menetapkan lantai awal. Kemudian, user menetapkan orang yang akan masuk ke dalam lift. 
Kapasitas lift sebanyak 8 orang. Apabila jumlah orang yang akan masuk ke dalam lift lebih dari 8 orang, program akan memberitahu jumlah orang yang tidak bisa masuk.
Kapasitas berat lift adalah 650 kg. Program akan menginput berat masing-masing orang yang akan masuk. Apabila lift melebihi kapasitas maksimum, orang yang terakhir masuk akan keluar sampai tidak melebihi kapasitas berat maksimum.
Masing-masing orang akan menginput lantai yang akan dituju. Ketika menginput lantai, program akan memvalidasi keberadaan lantai tersebut. Apabila lantai yang diinput tidak ada, program akan memberitahu user.
Apabila lantai yang dituju telah diinput, program akan memberitahu bahwa tombol lantai telah ditekan sebelumnya.
Setelah itu, lift akan beroperasi dengan bergerak ke atas sampai mencapai lantai paling atas yang telah diinput. Kemudian, lift akan bergerak ke bawah sesuai input user.

Kamus : 
lantai:str
cek_indexlantaiawal:int
validasi_inputlantaiawal:bool
input_lantaiawal:bool
list_berat:list
total_berat:float
count_databaselantai:int
inputlantai:int
validasi_inputlantai:str
listnaikindex:list
list_inputmentah:list
listnaik:list
posisiSekarang:int
list_turun:list
list_turunindex:list
list_beratorangturun:list
indexturun:int
orang_turun_double:int
k:int
masukan_lantaiawal:str
indexLantai:int
N:int
i:int
indexturunindex:int
index:int
orang_remain:int
"""

import time 
#Data Rujukan Lantai
lantai = ["B","LG","G","UG","1","2","3","5","7","8","9","10","11","12","15"]
#Variabel Input Lantai Awal
cek_indexlantaiawal = 0
validasi_inputlantaiawal = False
input_lantaiawal = False

#Cek Berat :
list_berat = [0 for i in range(8)]
total_berat = 0

#Validasi Input Lantai Naik dan Input Lantai Naik
count_databaselantai = 0
inputlantai = False
validasi_inputlantai = ""
listnaikindex = ["" for i in range(15)]
list_inputmentah = ["" for i in range(15)]
listnaik = [""for i in range(15)]
posisiSekarang = 0

#List Turun 
list_turun = ["" for i in range(15)]
list_turunindex = ["" for i in range(15)]
list_beratorangturun = ["" for i in range (8)]
indexturun = 0
orang_turun_double = 0
k = 0 #Variabel Manipulasi print
masukan_lantaiawal = ""
#Masukan Lantai Awal
while input_lantaiawal == False: #Validasi Input Lantai
    for l in lantai:
        print("┌───┐", end=" ")
    print()

    for l in lantai:
        print(f"│{l:^3}│", end=" ")
    print()

    for l in lantai:
        print("└───┘", end=" ")
    print()
    
    masukan_lantaiawal = input("Masukkan Lantai awal : ")
    masukan_lantaiawal = masukan_lantaiawal.upper()
    
    while cek_indexlantaiawal < len(lantai) and validasi_inputlantaiawal == False: #Cek Inputan apakah ada dalam database
        
        if masukan_lantaiawal == lantai[cek_indexlantaiawal]:
            validasi_inputlantaiawal = True
        
        else: 
            cek_indexlantaiawal +=1
    
    if validasi_inputlantaiawal == True: 
        input_lantaiawal = True
    
    else: 
        cek_indexlantaiawal = 0
        print("Lantai yang anda masukkan tidak sesuai")
#Naik ke lantai awal yang dipilih

indexLantai = cek_indexlantaiawal
if (indexLantai > posisiSekarang):
    for i in range(posisiSekarang + 1, indexLantai + 1):
        print(f"Lift naik ke {lantai[i]}.")
        time.sleep(1)

else:
    print(f"Lift sudah berada di lantai {lantai[indexLantai]}.")

if (indexLantai % 3 == 1):
    print(f"Lantai {lantai[indexLantai]}. Pintu bagian depan terbuka.")
    time.sleep(5)

else:
    print(f"Lantai {lantai[indexLantai]}. Pintu bagian belakang terbuka.")
    time.sleep(5)
    
# Program input orang dan cek berat
N = int(input("Masukkan jumlah orang yang akan masuk ke lift: "))

if N > 8:
    x = N - 8
    print(f"Jumlah orang yang tidak bisa masuk lift sebanyak {x}.")
    N = N - x

i = 1
while i <= N:
    list_berat[i - 1] = float(input(f"Masukkan berat orang ke-{i} (kg): "))
    i += 1

#Mengeluarkan orang terakhir yang masuk jika berat lebih dari kapasitas
i = 0
while i < N:
    total_berat = total_berat + list_berat[i]
    i += 1

while total_berat > 650:
    print(f"\nTotal berat {total_berat} kg melebihi kapasitas 650 kg.")
    print(f"Orang ke-{N} dengan berat {list_berat[N-1]} kg dikeluarkan.")

    total_berat = total_berat - list_berat[N-1]
    list_berat[N-1] = 0 
    N = N - 1


i = 0
count_databaselantai = 0
inputlantai = 0
indexturun = 0

#Alur Naik
for l in lantai:
    print("┌───┐", end=" ")
print()

for l in lantai:
    print(f"│{l:^3}│", end=" ")
print()

for l in lantai:
    print("└───┘", end=" ")
print()

#Validasi Input Lantai 
while inputlantai < N:
    masukancheck = input("Masukkan lantai : ")
    
    if masukancheck in list_inputmentah:
        pass
    
    else:
        list_inputmentah[i] = masukancheck
        list_inputmentah[i] = list_inputmentah[i].upper()
        validasi_inputlantai = "tidakada" # ada lantainya atau tidak
        count_databaselantai = cek_indexlantaiawal
    
    while count_databaselantai+1 < len(lantai) and validasi_inputlantai == "tidakada": # ada lantainya
        
        if list_inputmentah[i] == lantai[count_databaselantai+1]:
            validasi_inputlantai = "ada"
        
        else:
            count_databaselantai += 1
    
    if validasi_inputlantai == "tidakada": 
        count_databaselantai = 0
        
        while count_databaselantai < len(lantai) and validasi_inputlantai == "tidakada": # ada lantainya namun tidak diatas lantai saat ini
            
            if list_inputmentah[i] == lantai[indexLantai]:
                validasi_inputlantai = "lantai_saatini"
            
            elif list_inputmentah[i] == lantai[count_databaselantai]:
                validasi_inputlantai = "dibawahlantaiini"
            
            else:
                count_databaselantai += 1
    
    if validasi_inputlantai == "ada":
        count_databaselantai = cek_indexlantaiawal 
        validasi_inputlantai = ""
        print(list_inputmentah)
        i +=1
        inputlantai +=1
    
    elif validasi_inputlantai == "dibawahlantaiini": 
        
        if list_inputmentah[i] in list_turun:
            list_inputmentah[i]=""
            print("lantai yang dimasukkan sudah ditekan sebelumnya")
            orang_turun_double +=1
            indexturun +=1
            list_beratorangturun[indexturun] = list_berat[i]
            indexturun -=1
            inputlantai+=1
        
        else:    
            list_turun[indexturun]= list_inputmentah[i]
            list_inputmentah[i]=""
            print(f"Lantai {list_turun[indexturun]} akan dieksekusi setelah lift menyelesaikan proses naik sampai di lantai tujuan terakhir.")
            count_databaselantai = cek_indexlantaiawal
            list_beratorangturun[indexturun] = list_berat[i]
            inputlantai+=1
            indexturun +=1
        print(list_turun)
    
    elif validasi_inputlantai == "tidakada":
        print("lantai tidak ditemukan")
        count_databaselantai = cek_indexlantaiawal
        list_inputmentah[i]=""
    
    elif validasi_inputlantai == "lantai_saatini":
        print("Lantai yang anda pilih merupakan lantai saat ini")
        list_inputmentah[i]=""
    
    else:
        print("lantai yang dimasukkan sudah ditekan sebelumnya.")
        inputlantai +=1

#Sort List_inpumentah
index = 0
for i in range(len(lantai)):
    for j in range(len(list_inputmentah)):
        if list_inputmentah[j] == lantai[i]:
            listnaik[index] = list_inputmentah[j]
            index += 1
index = 0
#Mengubah listnaik yang sudah tersort (menjadi index yang sesuai di database Lantai)
for i in range(len(listnaik)):
    if listnaik[i]=="":
        listnaikindex[i]=""
    elif listnaik[i] in lantai: 
        listnaikindex[i]=lantai.index(listnaik[i])

#Print Lantai mulai naik
print("Lift mulai bergerak.")
posisiSekarang = cek_indexlantaiawal

while listnaikindex[k] != "":
    indexLantai = listnaikindex[k]
    
    if (indexLantai > posisiSekarang):
        
        for i in range(posisiSekarang + 1, indexLantai + 1):
            print(f"Lift naik ke {lantai[i]}.")
            time.sleep(1)
    
    else:
        print(f"Lift sudah berada di lantai {lantai[indexLantai]}.")

    posisiSekarang = indexLantai   

    if (indexLantai % 3 == 1):
        print(f"Lantai {lantai[indexLantai]}. Pintu bagian depan terbuka.")
        time.sleep(5)
        print("Pintu bagian depan tertutup.")
        time.sleep(3)
    
    else:
        print(f"Lantai {lantai[indexLantai]}. Pintu bagian belakang terbuka.")
        time.sleep(5)
        print("Pintu bagian belakang tertutup.")
        time.sleep(3)
    k+=1

#Input orang sesuai yang tersisa dan sisa tempat
orang_remain = indexturun +orang_turun_double
N = int(input("Masukkan jumlah orang yang akan masuk ke lift: "))

if N+orang_remain > 8:
    x = N+orang_remain - 8
    print(f"Jumlah orang yang tidak bisa masuk lift sebanyak {x}.")
    N = N +orang_remain- x

else:
    N = N + orang_remain

i = indexturun

while i < N:
    list_beratorangturun[i] = float(input(f"Masukkan berat orang ke-{i+1} (kg): "))
    i += 1

total_berat = 0
i = 0

while i < N:
    total_berat = total_berat + list_beratorangturun[i]
    i += 1

while total_berat > 650:
    print(f"\nTotal berat {total_berat} kg melebihi kapasitas 650 kg.")
    print(f"Orang ke-{N} dengan berat {list_beratorangturun[N-1]} kg dikeluarkan.")

    total_berat = total_berat - list_beratorangturun[N-1]
    list_beratorangturun[N-1] = 0 
    N = N - 1

print("pintu belakang tertutup")
#Alur Turun

for l in lantai:
    print("┌───┐", end=" ")
print()


for l in lantai:
    print(f"│{l:^3}│", end=" ")
print()

for l in lantai:
    print("└───┘", end=" ")
print()

i=0
inputlantai = indexturun
count_databaselantai = 0
#Validasi Input kembali

while inputlantai <N:
    masukancheck = input("Masukkan lantai : ")
    masukancheck = masukancheck.upper()
    
    if masukancheck in list_turun:
        pass
    
    elif masukancheck == lantai[posisiSekarang]:
        validasi_inputlantai = "lantai_saatini"
    
    else:
        list_turun[indexturun] = masukancheck
        list_turun[indexturun] = list_turun[indexturun].upper()
        validasi_inputlantai = "tidakada"
    
    while count_databaselantai < len(lantai) and validasi_inputlantai == "tidakada": #adalantainya
        
        if list_turun[indexturun] == lantai[count_databaselantai]:
            validasi_inputlantai = "ada"
        
        else:
            count_databaselantai += 1

    if validasi_inputlantai == "ada":
        count_databaselantai = posisiSekarang 
        
        while count_databaselantai < len(lantai) and validasi_inputlantai == "ada":
            
            if list_turun[indexturun] == lantai[count_databaselantai]:
                validasi_inputlantai = "diataslantaiini"
            
            else:
                count_databaselantai += 1
        
        if validasi_inputlantai == "diataslantaiini":
            print("Lantai yang dimasukkan berada di atas lantai ini. Lift hanya bisa turun ke lantai bawah.")
            list_turun[indexturun]=""
            validasi_inputlantai = ""
        
        else:
            validasi_inputlantai = ""
            inputlantai +=1
            indexturun +=1
            count_databaselantai = 0
    
    elif validasi_inputlantai == "tidakada": 
        print("Lantai tidak ditemukan")
        count_databaselantai = 0
        list_turun[indexturun]=""
    
    elif validasi_inputlantai =="lantai_saatini":
        print("Lantai yang anda pilih merupakan lantai saat ini")
    
    else:
        print("lantai yang dimasukkan sudah ditekan sebelumnya.")
        inputlantai+=1
    print(list_turun)

index = 0
#Sort List_turun agar dari besar ke kecil
for i in range(len(lantai)-1,-1,-1):
    for j in range(len(list_turun)):
        if list_turun[j] == lantai[i]:
            list_turunindex[index] = list_turun[j]
            index += 1

index =0
#Mengubah list_turun menjadi index
for i in range(len(list_turun)):
    if list_turunindex[i]=="":
        list_turunindex[i]=""
    
    elif list_turunindex[i] in lantai: 
        list_turunindex[i]=lantai.index(list_turunindex[i])
k=0

print("Lift mulai bergerak.")

while list_turunindex[k] != "":
    indexLantai = list_turunindex[k]
    
    if (indexLantai < posisiSekarang):
        
        for i in range(posisiSekarang - 1, indexLantai-1, -1):
            print(f"Lift turun ke {lantai[i]}.")
            time.sleep(1)
    
    else:
        print(f"Lift sudah berada di lantai {lantai[indexLantai]}.")

    posisiSekarang = indexLantai
   
    if (indexLantai % 3 == 1):
        print(f"Lantai {lantai[indexLantai]}. Pintu bagian depan terbuka.")
        time.sleep(5)
        print("Pintu bagian depan tertutup.")
        time.sleep(3)
    
    else:
        print(f"Lantai {lantai[indexLantai]}. Pintu bagian belakang terbuka.")
        time.sleep(5)
        print("Pintu bagian belakang tertutup.")
        time.sleep(3)
    k+=1 
