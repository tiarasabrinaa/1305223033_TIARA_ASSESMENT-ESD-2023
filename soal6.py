menu = {
    "Ayam Goreng Krispi": {"Tipe": "Makanan", "Harga": 15000},
    "Ayam Puk Puk (Bukan di geprek)": {"Tipe": "Makanan", "Harga": 13000},
    "Ayam Bakar": {"Tipe": "Makanan", "Harga": 20000},
    "Es teh": {"Tipe": "Minuman", "Harga": 5000},
    "Es Jeruk": {"Tipe": "Minuman", "Harga": 7000}
}

def hitung_total_harga(pesanan):
    total_harga = 0
    pajak_makanan = 0.05
    pajak_minuman = 0.03
    pajak_transaksi = 0.15

    for item, jumlah in pesanan.items():
        harga = menu[item]["Harga"]
        tipe_item = menu[item]["Tipe"]
        total_item = harga * jumlah

        if tipe_item == "Makanan":
            total_item += total_item * pajak_makanan
        else:
            total_item += total_item * pajak_minuman

        total_harga += total_item

    total_harga += total_harga * pajak_transaksi
    return total_harga

rehan = {"Ayam Bakar": 2, "Es teh": 1}
amba = {"Ayam Puk Puk (Bukan di geprek)": 1, "Es teh": 3}
faiz = {"Ayam Goreng Krispi": 1, "Ayam Puk Puk (Bukan di geprek)": 1, "Ayam Bakar": 1, "Es teh": 1, "Es Jeruk": 1}

total_rehan = hitung_total_harga(rehan)
total_amba = hitung_total_harga(amba)
total_faiz = hitung_total_harga(faiz)

print("Total biaya yang harus dibayar oleh Rehan Whangsap:", total_rehan)
print("Total biaya yang harus dibayar oleh Amba Roni:", total_amba)
print("Total biaya yang harus dibayar oleh Faiz ngawi:", total_faiz)
