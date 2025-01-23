#memanggil function yang ada di file mymodule.py
#artinya file mymodule.py itu merupakan module

#import modulenya
import mymodule
#panggil module.nama_function()
mymodule.sayHi("Cika")
text = "and my friend is " + mymodule.friend
print(text)