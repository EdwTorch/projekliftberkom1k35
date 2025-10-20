import time
lantai = ["B","LG","G","UG","1","2","3","5","7","8","9","10","11","12","15"]
countCheck = 0
beratMaks = 1500
ada = ""
cekdobellantai = False
listnaikindex =["" for i in range(15)]
masukandalam = ["" for i in range(15)]
listnaik = [""for i in range(15)]
inputlantai = False
k=0
posisiSekarang = 0
print("Lift Anda sedang berada di Lantai B. Pintu belakang sudah terbuka.")
berat = float(input("Masukkan berat (kg): "))
#State_Naik
if (berat <= beratMaks):
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
    while inputlantai == False:
        masukancheck = input("Masukkan lantai : ")
        if masukancheck in masukandalam:
            pass
        else:
            masukandalam[i] = masukancheck
            masukandalam[i] = masukandalam[i].upper()
            ada = "tidakada" # ada lantainya atau tidak
        while countCheck < len(lantai) and ada == "tidakada": # ada lantainya
            if masukandalam[i] == lantai[countCheck]:
                ada = "ada"
            else:
                countCheck += 1
        if ada == "ada":
            countCheck = 0 
            ada = ""
            selesai = int(input("Apakah sudah selesai (Ketik 1 jika sudah selesai, Ketik 0 jika belum selesai) : "))
            print(masukandalam)
        if selesai == 1:
            inputlantai = True
        elif selesai ==0:
            i += 1
        elif ada == "tidakada": 
            print("Lantai tidak ditemukan")
            countCheck = 0
            masukandalam[i]=""
        else:
            print("lantai yang dimasukkan sudah ditekan sebelumnya.")
    index = 0
    for i in range(len(lantai)):
        for j in range(len(masukandalam)):
            if masukandalam[j] == lantai[i]:
                listnaik[index] = masukandalam[j]
                index += 1
    index =0
    for i in range(len(listnaik)):
        if listnaik[i]=="":
            listnaikindex[i]=""
        elif listnaik[i] in lantai: 
            listnaikindex[i]=lantai.index(listnaik[i])
    print(listnaikindex[0])
    print("Lift mulai bergerak.")
    while listnaikindex[k] != "":
        indexLantai = listnaikindex[k]
        if (indexLantai > posisiSekarang):
            for i in range(posisiSekarang + 1, indexLantai + 1):
                print(f"Lift naik ke {lantai[i]}.")
                time.sleep(1)
        elif (indexLantai < posisiSekarang):
            for i in range(posisiSekarang - 1, indexLantai - 1, -1):
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

else:
    print("Lift berbunyi, tolong kurangi beban.")
    while berat > beratMaks:
        kurangiBeban = float(input("Masukkan berat yang dikurangi (kg): "))
        berat -= kurangiBeban
        if berat > beratMaks:
            print(f"Lift masih berbunyi, tolong kurangi beban lagi. Beban saat ini : {berat}")
        else:
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
            while inputlantai == False:
                masukancheck = input("Masukkan lantai : ")
                if masukancheck in masukandalam:
                    pass
                else:
                    masukandalam[i] = masukancheck
                    masukandalam[i] = masukandalam[i].upper()
                    ada = "tidakada"
                while countCheck < len(lantai) and ada == "tidakada": #adalantainya
                    if masukandalam[i] == lantai[countCheck]:
                        ada = "ada"
                    else:
                        countCheck += 1
                if ada == "ada":
                    countCheck = 0 
                    ada = ""
                    selesai = int(input("Apakah sudah selesai (Ketik 1 jika sudah selesai, Ketik 0 jika belum selesai) : "))
                    print(masukandalam)
                    if selesai == 1:
                        inputlantai = True
                    elif selesai ==0:
                        i += 1
                elif ada == "tidakada": 
                    print("Lantai tidak ditemukan")
                    countCheck = 0
                    masukandalam[i]=""
                else:
                    print("lantai yang dimasukkan sudah ditekan sebelumnya.")
            index = 0
            for i in range(len(lantai)):
                for j in range(len(masukandalam)):
                    if masukandalam[j] == lantai[i]:
                        listnaik[index] = masukandalam[j]
                        index += 1
            index =0
            for i in range(len(listnaik)):
                if listnaik[i]=="":
                    listnaikindex[i]=""
                elif listnaik[i] in lantai: 
                    listnaikindex[i]=lantai.index(listnaik[i])
            print("Lift mulai bergerak.")
            while listnaikindex[k] != "":
                indexLantai = listnaikindex[k]
                if (indexLantai > posisiSekarang):
                    for i in range(posisiSekarang + 1, indexLantai + 1):
                        print(f"Lift naik ke {lantai[i]}.")
                        time.sleep(1)
                elif (indexLantai < posisiSekarang):
                    for i in range(posisiSekarang - 1, indexLantai - 1, -1):
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
