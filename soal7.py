def dekripsi(pesan_terenkripsi):
    pesan_didekripsi = ""
    for char in pesan_terenkripsi:
        if char.isalpha():
            unicode_val = ord(char) - 5
            if char.islower():
                if unicode_val < ord('a'):
                    unicode_val += 26
            else:
                if unicode_val < ord('A'):
                    unicode_val += 26
            pesan_didekripsi += chr(unicode_val)
        else:
            pesan_didekripsi += char
    return pesan_didekripsi

print("Pesan yang sudah didekripsi:")
print("i.\t", dekripsi("xfqfr bfmdz"))
print("ii.\t", dekripsi("gjxtp lzj rfz ifkyfw jxi snm"))
print("iii.\t", dekripsi("gwt, gjxtp qz rfz rfpfs in bfwlty lfp?"))
print("iv.\t", dekripsi("fpz xfdfsl pfrz, rfz lfp ofin ufhfwpz"))
print("v.\t", dekripsi("dfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"))