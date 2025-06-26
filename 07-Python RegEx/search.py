import re #menggunakan module regex

#search

text = "Halo namaku Refina, aku sedang belajar python"
#tambahan text dari variable text di atas
text += " umurku 67 tahun"
posisi = "posisi 1"
#menampilkan angka pertama yang cocok jika menggunakan search & (/d)
search1 = re.search(r"\d", text)
search_posisi = re.search(r"\d", posisi)

print(search1)

print(search1.span())
print(search_posisi.span())
print(search1.group())