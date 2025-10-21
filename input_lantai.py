import time
input_lantaiawal = False
masukan_lantaiawal = ""
lantai = ["B","LG","G","UG","1","2","3","5","7","8","9","10","11","12","15"]
lantaiawal = ""
cek_indexlantaiawal = 0
validasi_inputlantaiawal = False
indexLantai = 0
posisiSekarang = 0
while input_lantaiawal == False:
    masukan_lantaiawal = input("Masukkan Lantai awal : ")
    while cek_indexlantaiawal < len(lantai) and validasi_inputlantaiawal == False:
        if masukan_lantaiawal == lantai[cek_indexlantaiawal]:
            validasi_inputlantaiawal = True
        else: 
            cek_indexlantaiawal +=1
    if validasi_inputlantaiawal == True: 
        input_lantaiawal = True
    else: 
        cek_indexlantaiawal = 0
        print("Lantai yang anda masukkan tidak sesuai")

indexLantai = cek_indexlantaiawal
if (indexLantai > posisiSekarang):
    for i in range(posisiSekarang + 1, indexLantai + 1):
        print(f"Lift naik ke {lantai[i]}.")
        time.sleep(1)
else:
    print(f"Lift sudah berada di lantai {lantai[indexLantai]}.")

    
    