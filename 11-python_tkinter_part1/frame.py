import tkinter as tk 
window = tk.Tk()
window.title("Learn Frame")
window.geometry("400x200") #lebar x tinggi
frame_title = tk.Frame(
    master = window,
    height = 100,
    width = 200,
    bg = "pink"
)

label_title = tk.Label(
    master = frame_title,
    text = "Frame for Widget", #menampilkan text label
    foreground = "black", #warna tulisan
    font = ("Times New Roman", 20), #jenis & ukurann huruf
)
label_title.pack()


frame_desc = tk.Frame(
    master = window,
    height = 100,
    width = 200,
    bg = "yellow"
)


label_desc = tk.Label(
    master = frame_desc,
    text = "Deskripsinya kita sedang belajar python tkinter frame"
)
label_desc.pack()

frame_title.pack()

frame_desc.pack()

#looping
window.mainloop()