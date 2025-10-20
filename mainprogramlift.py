import time
lantai = ["B","LG","G","UG","1","2","3","5","7","8","9","10","11","12","15"]
count_databaselantai = 0
beratMaks = 1500
validasi_inputlantai = ""
listnaikindex =["" for i in range(15)]
list_inputmentah = ["" for i in range(15)]
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
        if masukancheck in list_inputmentah:
            pass
        else:
            list_inputmentah[i] = masukancheck
            list_inputmentah[i] = list_inputmentah[i].upper()
            validasi_inputlantai = "tidakada" # ada lantainya atau tidak
        while count_databaselantai < len(lantai) and validasi_inputlantai == "tidakada": # ada lantainya
            if list_inputmentah[i] == lantai[count_databaselantai]:
                validasi_inputlantai = "ada"
            else:
                count_databaselantai += 1
        if validasi_inputlantai == "ada":
            count_databaselantai = 0 
            validasi_inputlantai = ""
            selesai = int(input("Apakah sudah selesai (Ketik 1 jika sudah selesai, Ketik 0 jika belum selesai) : "))
            print(list_inputmentah)
        if selesai == 1:
            inputlantai = True
        elif selesai ==0:
            i += 1
        elif validasi_inputlantai == "tidakada": 
            print("Lantai tidak ditemukan")
            count_databaselantai = 0
            list_inputmentah[i]=""
        else:
            print("lantai yang dimasukkan sudah ditekan sebelumnya.")
    index = 0
    #Sort List_inpumentah
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
    print(listnaikindex[0])
    print("Lift mulai bergerak.")
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
                if masukancheck in list_inputmentah:
                    pass
                else:
                    list_inputmentah[i] = masukancheck
                    list_inputmentah[i] = list_inputmentah[i].upper()
                    validasi_inputlantai = "tidakada"
                while count_databaselantai < len(lantai) and validasi_inputlantai == "tidakada": #adalantainya
                    if list_inputmentah[i] == lantai[count_databaselantai]:
                        validasi_inputlantai = "ada"
                    else:
                        count_databaselantai += 1
                if validasi_inputlantai == "ada":
                    count_databaselantai = 0 
                    validasi_inputlantai = ""
                    selesai = int(input("Apakah sudah selesai (Ketik 1 jika sudah selesai, Ketik 0 jika belum selesai) : "))
                    print(list_inputmentah)
                    if selesai == 1:
                        inputlantai = True
                    elif selesai ==0:
                        i += 1
                elif validasi_inputlantai == "tidakada": 
                    print("Lantai tidak ditemukan")
                    count_databaselantai = 0
                    list_inputmentah[i]=""
                else:
                    print("lantai yang dimasukkan sudah ditekan sebelumnya.")
            index = 0
            for i in range(len(lantai)):
                for j in range(len(list_inputmentah)):
                    if list_inputmentah[j] == lantai[i]:
                        listnaik[index] = list_inputmentah[j]
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
