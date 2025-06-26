'''
MEMBUAT FILE X untuk membuat file baru, dia akan eror jika file yang dibuat sudah ada sebelumnya
'''
#file = open("nama_file_yang_akan_dibuat","x")
# file = open("alhazen-pythonHighJump-group/03-File Handling/fileku.txt", "x")

# file = open("read_file.py","x")

#jika mau dimasukkan ke dalam folder yang dimau, maka folder/filenya

# file = open("alhazen-pythonHighJump-group/03-File Handling/read.py", "x")

'''
MEMBACA FILE MENGGUNAKAN r
nantinya akan ditampilkan di terminal vscode/di command line
jika tidak ditemukan filenya, maka akan muncul eror
'''
file = open("alhazen-pythonHighJump-group/03-File Handling/read.py", "r")
print(file.read())

# file = open("baca.py", "r")
# print(file.read())

# file = open("alhazen-pythonHighJump-group/03-File Handling/write.py", "x")

'''
MENULIS FILE (RITE) Menggunakan w
'''
file = open("alhazen-pythonHighJump-group/03-File Handling/fileku.txt", "w")
sayHi = "Hi aku sedang belajar python file handling!\n"
file.write(sayHi)
file.write("Ini seru banget loh!")
file.close()#close file jika sudah selesai write

file = open("alhazen-pythonHighJump-group/03-File Handling/write.txt", "w")
text1 = "Hi ini program python ku!"
file.write(text1)

file = open("alhazen-pythonHighJump-group/03-File Handling/write.txt", "w")
text2 = "Hi ini program python kedua ku!"
file.write(text2)

#jika menggunakan write di bawah ini tidak akan replace (tergantikan)
file.write("ini python\n")
file.write("hai")


'''
NOTES:
1. perintah x (create) akan menambahkan file baru, jika file nya sudah terbuat sebelumnya tapi
    kamu menggunakan perintah x, maka akan terjadi eror
2. perintah r (read) akan membaca isi file, isinya ditampilkan di commandline/terminal vscode,
    jika file nya tidak ada/tidak ditemukan, akan terjadi eror
3. perintah w (write) akan membuat/menulis isi di dalam file yang dipanggil, 
    jika file nya tidak ada/tidak ditemukan, otomatis akan membuat file sendiri sesuai dengan file yang kalian panggil/tuliskan (tidak akan terjadi eror)
4. perintah a (append) akan menambahkan tulisan, berbeda dengan w yang sifatnya replace, append ini akan menambahan tulisan setiap kali di run,
    jika file nya tidak ada/tidak ditemukan, otomatis akan membuat file sendiri sesuai dengan file yang kalian panggil/tuliskan (tidak akan terjadi eror)
'''