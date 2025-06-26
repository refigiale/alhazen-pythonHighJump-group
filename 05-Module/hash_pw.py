#kita akan hashing password (mengubah password menjadi angka dan huruf secara acak ketika disimpan)

import hashlib
admin_password = "admin123"
var_endcode = admin_password.encode('utf-8')
var_hash = hashlib.md5(var_endcode).hexdigest()
print(var_endcode)