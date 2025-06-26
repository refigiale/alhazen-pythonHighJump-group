class Pekerjaan:
    def __init__(self, kategori, nama_pekerjaan):
        self.kategori = kategori
        self.nama_pekerjaan = nama_pekerjaan

    def kegiatan(self):
        text = str(self.nama_pekerjaan) + " sedang menyanyi"
        return(text)

object1= Pekerjaan("kesehatan", "dokter")
object2 = Pekerjaan("musik", "penyanyi")
#dokter merupakan pekerjaan di bidang kesehatan
print(object1.nama_pekerjaan, "merupakan pekerjaan di bidang", object1.kategori)

#salah satu pekerjaan di bidang kesehatan adalah dokter
print("salah satu pekerjaan di bidang", object1.kategori, "adalah", object1.nama_pekerjaan)
print(object2.kegiatan())


