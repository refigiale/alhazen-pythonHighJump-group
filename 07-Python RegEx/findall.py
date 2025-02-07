import re #menggunakan module regex

#findall

text = "Halo namaku Refina, aku sedang belajar python"
#tambahan text dari variable text di atas
text += " umurku 19 tahun"

#menampilkan angka yang ada di text (0-9)
find = re.findall(r"\d", text)

print(text)
#menampilkan findall
print(f"angka yang akan keluar adalah: {find}")

#mencoba menampilkan kata yang tidak ada di dalam variable text
temukan = re.findall(r"hubungan", text) #mencari kata "hubungan" dari variable text
print(temukan) #jika kata nya tidak ditemukan, maka akan menampilkan list kosong

