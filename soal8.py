produk = [
    {"Produk": "TV", "Kategori": "elektronik", "Harga": 1000},
    {"Produk": "headphone", "Kategori": "elektronik", "Harga": 200},
    {"Produk": "baju", "Kategori": "fashion", "Harga": 50},
    {"Produk": "gitar", "Kategori": "musik", "Harga": 300},
    {"Produk": "sepatu", "Kategori": "olahraga", "Harga": 80},
    {"Produk": "kamera", "Kategori": "elektronik", "Harga": 600}
]

pelanggan = {
    "Rina": {"Minat": ["elektronik", "musik"], "Beli": ["TV", "headphone"]},
    "Budi" : {"Minat": ["fashion", "musik"], "Beli": ["baju", "gitar"]},
    "Hartono": {"Minat": ["olahraga", "elektronik"], "Beli": ["sepatu", "kamera"]}
}

def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = pelanggan[nama_pelanggan]["Minat"]
    beli_pelanggan = pelanggan[nama_pelanggan]["Beli"]

    rekomendasi = []
    for item in produk:
        if item["Kategori"] in minat_pelanggan:
            rekomendasi.append(item["Produk"])

    return rekomendasi

hasil_rekomendasi = rekomendasi_produk("Rina")
print("Rina \t\t:", hasil_rekomendasi)

hasil_rekomendasi = rekomendasi_produk("Budi")
print("Budi \t\t:", hasil_rekomendasi)

hasil_rekomendasi = rekomendasi_produk("Hartono")
print("Hartono \t:", hasil_rekomendasi)