N = int(input("Masukkan jumlah orang yang akan masuk ke lift: "))

if N > 8:
    x = N - 8
    print(f"Jumlah orang yang tidak bisa masuk lift sebanyak {x}.")
    N = N - x

i = 1
list_berat = [0 for i in range(8)]

while i <= N:
    list_berat[i - 1] = float(input(f"Masukkan berat orang ke-{i} (kg): "))
    i += 1

total_berat = 0
i = 0
while i < N:
    total_berat = total_berat + list_berat[i]
    i += 1

while total_berat > 650:
    print(f"\nTotal berat {total_berat} kg melebihi kapasitas 650 kg.")
    print(f"Orang ke-{N} dengan berat {list_berat[N-1]} kg dikeluarkan.")
    N = N - 1
    
    total_berat = 0
    i = 0
    while i < N:
        total_berat = total_berat + list_berat[i]
        i += 1

if total_berat <= 650:
    print(f"\nLift jalan dengan {N} orang. Total berat: {total_berat} kg.")
    print("Jalankan program lift...")
else:
    print("\nLift tidak bisa jalan. Kurangi beban lebih banyak.")