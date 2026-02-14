print("========================================KALKULATOR SEDERHANA UPGRADE PROYEK 1 INES============================================")
#perbedaannya dengan yang "kalkulatorSederhana" adalah krn disini menggunakan list 

ListOperasi = ["+", "-", "*","**","%","/","//"]
print(ListOperasi)

ANGKA = int(input("masukkan angka : "))  
while True:
    OPERASI = input("masukkan operasi : ") 
    if OPERASI == "exit" :
        print("ketik 'exit' akan mengarhkan anada selesai dari kalkulator sederhana nesi")
        break
    if OPERASI not in ListOperasi:
        print("operasi tidak bisa dijlnkan")
        continue
    
    NEXT = int(input("masukkan angka berikutnya : ")) 
    if OPERASI == "+" :
        ANGKA += NEXT
    elif OPERASI == "-" : 
        ANGKA -= NEXT
    elif OPERASI == "*":
        ANGKA *= NEXT
    elif OPERASI == "/":
        ANGKA /= NEXT
    elif OPERASI == "//":
        if NEXT == 0:
            print("hasilnya adalah : tidak bisa dibagi 0")
            continue
        ANGKA //= NEXT
    elif OPERASI == "%" : 
        ANGKA %= NEXT
    elif OPERASI == "**":
        ANGKA **= NEXT
    print("hasil sementara adalah : ", ANGKA)
    
hasil = ANGKA
print("hasil akhir adalah : ", hasil )    

for i in range(3) :
    penilaian = input("masukkan penilaian mu (ya)/(tidak) : ")
    if penilaian.lower() == "ya" :
        print("cuttie and helpful")
    else:
        print("i will fix it")



    