def username(nama):
    jumlah_huruf_unik = len(set(nama))

    #Menghitung jumlah kombinasi untuk panjang username 1 hingga 6 dengan asumsi semua huruf bisa
    #digunakan lebih dari 1 kali

    total_kombinasi = 0
    for i in range(1, 7):
        total_kombinasi += jumlah_huruf_unik ** i

    return total_kombinasi

nama = "NaipLovyu"
print("Jumlah kombinasi username yang mungkin (dengan pengulangan huruf):", username(nama))
