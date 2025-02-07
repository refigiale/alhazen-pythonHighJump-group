import re

#split

text = "Halo namaku Refina, aku sedang belajar python"
#tambahan text dari variable text di atas
text += " umurku 19 tahun"

print(text)

split1 = re.split(r"\s", text)
print(split1)

split2 = re.split(r"\s", text, 3)
print(split2)