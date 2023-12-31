from collections import Counter

def identifikasi_anak_nakal(nama_anak):
    counter_nama = Counter(nama_anak)
    if counter_nama:
        nama_terbanyak = counter_nama.most_common(1)[0][0]
        jumlah_terbanyak = counter_nama.most_common(1)[0][1]

        if jumlah_terbanyak == len(nama_anak) or jumlah_terbanyak == 1:
            return "Semuanya anak baik"
        else:
            nama_anak_nakal = [nama for nama, jumlah in counter_nama.items() if jumlah == jumlah_terbanyak]
            return f"{' dan '.join(nama_anak_nakal)} Nackal"
    else:
        return "Tidak ada data anak"

data_1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
data_2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
data_3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]

print("Input 1\t:", identifikasi_anak_nakal(data_1))
print("Input 2\t:", identifikasi_anak_nakal(data_2))
print("Input 3\t:", identifikasi_anak_nakal(data_3))
