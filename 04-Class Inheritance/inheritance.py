class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
class student(Person):
    pass

object1 = student("Refina", 19)
object2 = Person("Ahmad", 17)
print(object1.nama, "berumur", object1.umur, "tahun")
print(object2.nama, "berumur", object2.umur, "tahun")

