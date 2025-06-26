import re

#sub
#replace (mengganti)

text = "Halo namaku Refina, aku sedang belajar python"
#tambahan text dari variable text di atas
text += " umurku 19 tahun"

print(text)
#\s = mencari spasi/mencocokkan spasi
sub1 = re.sub(r"\s", "_", text)
print(sub1)

#bisa diatur replace nya mau berapa banyak menggunakan parameter di akhir
sub2 = re.sub(r"\s", "_", text,2)
print(sub2)