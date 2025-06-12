#INTERACTIVE GUI

import tkinter as tk

#backend/bagian logic nya
def checkNumber():#function cek nomor
    nomor = int(input_angka.get()) #mengambil nomor dari inputan/text input/entry

    if nomor %2 == 0:#jika hasil bagi 2 nya sama dengan 0
        text_hasil['text'] = f"{nomor}"
        text_hasil['text'] += " adalah bilangan genap"
        input_angka.delete(0, tk.END)    
    else:
        text_hasil['text'] = f"{nomor}"
        text_hasil['text'] += " adalah bilangan ganjil"
        input_angka.delete(0, tk.END)  
#-----------------------------Function dibuat sebelum button agar bisa dipanggil---------------------------------
window = tk.Tk()
window.title("Interactive GUI Python")
window.geometry("400x200")
window['bg'] = 'cyan'
judul = tk.Label(
    text="Bilangan Genap atau Bilangan Ganjil?",
    foreground="blue",
    background="white",
    height=4,
    width=27,
    font= ("Times New Roman", 16)
)
judul.pack()

input_angka = tk.Entry(
    font = ("Times New Roman", 12),
)
input_angka.pack()

tombol_cek = tk.Button(
    text = "Check Nomor",
    command = checkNumber
)
tombol_cek.pack()

text_hasil = tk.Label(
    font=("Arial", 12)
)
text_hasil.pack()



window.mainloop()



