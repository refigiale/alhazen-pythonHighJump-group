import tkinter as tk 

window = tk.Tk()
window.title("Learn Frame") #judul tab
window.geometry("400x200") # lebar x tinggi (ukuran window)

# Frame Title
frame_title = tk.Frame(
    master=window,#mengirimkan frame ke window
    height=100, #tinggi
    width=200, #lebar
    bg="pink" #background
)
frame_title.pack(fill="both", expand=True)  # Tambahkan fill (mengisi ruang kosong) dan expand (memperluas frame agar ruang yg ada di window)agar terlihat


label_title = tk.Label(
    master=frame_title, #mengirim label ke frame title
    text="Frame for Widget",  # menampilkan teks label
    foreground="black",  # warna tulisan
    font=("Times New Roman", 20),  # jenis & ukuran huruf
)
label_title.pack()

# Frame Description
frame_desc = tk.Frame(
    master=window,
    height=50,
    width=100,
    bg="yellow"
)
frame_desc.pack(fill="both", expand=True)  # Tambahkan fill dan expand agar terlihat

label_desc = tk.Label(
    master=frame_desc,
    text="Deskripsinya kita sedang belajar python tkinter frame"
)
label_desc.pack()

# Looping
window.mainloop()
