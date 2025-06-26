#import package tkinter

import tkinter as tk #nama modul tkinter tapi dipersingkat jadi tk

#membuat window
#panggil modul.function()
window = tk.Tk() #variable window berisi function Tk() tk (nama modul nya)

#membuat judul window/halaman
window.title("My Python App")

#mengatur ukuran window/halaman
window.geometry("400x400")

#mengatur latar belakang window/background
window['bg'] = 'pink'

#masukkan nama gambar, masukkan di folder yg sama dengan file project
icon = tk.PhotoImage(file='home icon.png')

window.tk.call('wm', 'iconphoto', window._w, icon)

#MENAMPILKAN LABEL
label = tk.Label(
    text = "Hello Kodingersss Friend!", #menampilkan text label
    foreground = "white", #warna tulisan
    background = "blue", #warna bg
    height = 4, #tinggi bg
    width = 20, #lebar bg 
    font = ("Times New Roman", 20), #jenis & ukurann huruf
)

label.pack() #memasukkan widget ke window agar labelnya terlihat


#MENAMPILKAN INPUTAN SATU BARIS MENGGUNAKAN Entry()
isi = tk.Entry(
    font = ("Arial, 14"),
    foreground = "black",
)
isi.pack()


#MENAMPILKAN INPUTAN BEBERAPA BARIS MENGGUNAKAN Text()
text_box = tk.Text(
    font = ("Arial, 14"),
    foreground = "black",
    height = 3,
    width = 7
)
text_box.pack()

#MENAMPILKAN TOMBOL
tombol = tk.Button(
    text = "Next", #menampilkan text tombol
    foreground = "red", #warna tulisan
    background = "yellow", #warna bg
    height = 1, #tinggi bg
    width = 4, #lebar bg 
    font = ("Robotto", 12), #jenis & ukurann huruf
)
tombol.pack() #namavariable.pack(), pack() adalah function memasukkan widget ke window agar buttonnya terlihat

#looping
window.mainloop()
