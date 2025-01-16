


bahasa_pemrograman = ["python", "javascript", "php"]
framework = ["laravel", "django", "vue.js"]

#ini write
file = open("alhazen-pythonHighJump-group/03-File Handling/note_for_append.txt","w")
file.write("Lihat di bawah ini\n")
for text in bahasa_pemrograman:
    file.write(f"aku belajar {text}\n")
#ini append
file = open("alhazen-pythonHighJump-group/03-File Handling/note_for_append.txt","a")
file.write("Framework yang aku pelajari\n")
for text in framework:
    file.write(f"{text}\n")
file.close

file = open("alhazen-pythonHighJump-group/03-File Handling/note_for_append.txt","r")
print(file.read())

#jadi, jika menggunakan method write, setiap running jika isi filenya dditambah maka isinya akan terupdate atau tergantikan (replace)
#jika menggunakan append, maka isinya akan bertambah