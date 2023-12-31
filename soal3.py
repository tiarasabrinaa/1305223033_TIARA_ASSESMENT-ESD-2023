def cek_pencuri():
    urutan_teman = ["Ningguang", "Hutao", "Xiao", "Childe"]
    kebiasaan_teman = {
        "Ningguang": ["memeriksa kue", "memberikan kado"],
        "Hutao": ["memberikan kado"],
        "Xiao": ["memotret"],
        "Childe": ["membawa air mineral", "meletakkan air mineral di meja", "memberikan kado"]
    }
    
    foto = "utuh" #sesuai deskripsi soal
    
    orang_dicurigai = []
    cek_setelah_xiao = False #karena foto xiao utuh, orang sebelum xiao pasti tidak mengambil
    
    for teman in urutan_teman:
        if cek_setelah_xiao:
            orang_dicurigai.append(teman) #orang setelah xiao mungkin mengambil
        
        if teman == "Xiao":
            orang_dicurigai.append(teman) #xiao bisa saja mengambil setelah memfoto
            cek_setelah_xiao = True
        
        for dicurigai in orang_dicurigai[:]:
            kegiatan_terakhir = kebiasaan_teman[dicurigai][-1]
            if kegiatan_terakhir == "memberikan kado": #jika aktivitas terakhir memberi kado, hapus kecurigaan karena saat memberi kado akan ketauan abah jika mencuri
                orang_dicurigai.remove(dicurigai)
        
        # Jika sisa satu orang yang dicurigai, kembalikan nama orang tersebut
        if len(orang_dicurigai) == 1:
            return orang_dicurigai[0]
    
    return None  # Jika tidak ada solusi

pencuri = cek_pencuri()
if pencuri:
    print(f"Pencuri kemungkinan adalah: {pencuri}")
else:
    print("Tidak dapat menentukan siapa pencurinya.")
