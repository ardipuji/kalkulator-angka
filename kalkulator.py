total = 0.0
lanjutkan = True

print("\n========== KALKULATOR ==========")
while True:
    try:
        angka = float(input("Masukkan angka: "))
        total += angka
        break
    except ValueError:
        print("---> Input tidak valid, silakan masukkan angka!\n")

while lanjutkan:
    operator = input("Masukkan operator (+, -, *, /) atau (=) untuk menghitung: ")
    
    if operator == "=":
        lanjutkan = False
    elif operator in ("+", "-", "*", "/"):
        while True:
            try:
                angka = float(input("Masukkan angka: "))
                if operator == "/" and angka == 0:
                    print("---> Tidak bisa membagi dengan nol! Masukkan angka lain.\n")
                else:
                    break
            except ValueError:
                print("---> Input tidak valid, silakan masukkan angka!\n")
        
        if operator == "+":
            total += angka
        elif operator == "-":
            total -= angka
        elif operator == "*":
            total *= angka
        elif operator == "/":
            total /= angka
            
        print(f"---> Hasil sementara: {total}\n")
    else:
        print("---> Operator tidak valid, silakan masukkan operator yang benar!\n")

print("\n========== HASIL ==========")
print(f"Hasilnya adalah : {total}")