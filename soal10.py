def hitung_kembalian(total_pembayaran, total_belanja):
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = total_pembayaran - total_belanja
    hasil_kembalian = {}

    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah = kembalian // pecahan
            hasil_kembalian[str(pecahan)] = jumlah
            kembalian %= pecahan

    hasil_kembalian = {k: hasil_kembalian[k] for k in sorted(hasil_kembalian, key=int)}
    return hasil_kembalian

test_cases = [
    (10000, 7500),
    (5000, 1100),
    (178000, 90500)
]

for total_pembayaran, total_belanja in test_cases:
    print(f"Total Pembayaran: {total_pembayaran}")
    print(f"Total Belanja: {total_belanja}")
    kembalian = hitung_kembalian(total_pembayaran, total_belanja)
    print(kembalian)
    print()