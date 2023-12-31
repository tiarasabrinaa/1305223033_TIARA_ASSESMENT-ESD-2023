def hitung_kombinasi_username(nama_lengkap, panjang_username):
    nama_lengkap = nama_lengkap.replace(" ", "")
    jumlah_huruf = len(nama_lengkap)

    def faktorial(n):
        if n == 0:
            return 1
        else:
            return n * faktorial(n - 1)

    def kombinasi(n, k):
        return faktorial(n) // (faktorial(k) * faktorial(n - k))

    total_kombinasi = 0
    for i in range(1, panjang_username + 1):
        total_kombinasi += kombinasi(jumlah_huruf, i)

    return total_kombinasi

nama = "Naip Lovyu"
panjang_username = 6

jumlah_kombinasi = hitung_kombinasi_username(nama, panjang_username)
print("Jumlah total kombinasi username yang mungkin:", jumlah_kombinasi)
