def cekPalindrom(kata):
  k = len(kata) - 1
  polindrom = True
  for i in range(0,len(kata)//2):
    if kata[i]!=kata[k]:
      polindrom = False
      break
    k = k-1
  if polindrom==True:
    return "eureeka!"
  else:
    return "suka blyat"

print("Angsa \t\t\t: ", cekPalindrom("Angsa"))
print("KataK \t\t\t: ", cekPalindrom("KataK"))
print("kasur empuk \t\t: ", cekPalindrom("kasur empuk"))
print("Aku Suka Kamu \t\t: ", cekPalindrom("Aku Suka Kamu"))
print("Ibu Ratna antar ubi. \t: ", cekPalindrom("Ibu Ratna antar ubi."))