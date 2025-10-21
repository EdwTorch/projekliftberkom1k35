batas_orang = 8
berat_maks = 650

jumlah_orang = int(input("Masukkan jumlah orang yang akan masuk dalam lift: "))

if jumlah_orang > batas_orang:
    print("Jumlah orang melebihi kapasitas lift.")
else:
    berat_total = 0
    for i in range(1, jumlah_orang + 1):
        berat_individu = float(input(f"Masukkan berat orang ke-{i} (kg): "))
        berat_total += berat_individu

    if berat_total > berat_maks:
        print(f"Beban melebihi kapasitas lift. Total berat = {berat_total} kg, maksimum = {berat_maks} kg")
    else:
        print(f"Lift jalan. Total berat = {berat_total} kg")