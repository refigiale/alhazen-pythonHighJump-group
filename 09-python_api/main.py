#1.pip install requests di terminal atau di command line (cmd)
#2.import requests

import requests

import json

url = "https://jsonplaceholder.typicode.com/todos" #alamat api nya

response = requests.get(url) #menggunakan method get (mengambil data)

print(type(response)) #print tipe data dari var response

print(response) #print response
#menampilkan <Response [200]> yang berarti response sukses

data = response.json()
for todo in data:
    if todo["userId"] == 4: #mengambil data yang userId nya = 4
        json_object = json.dumps(todo, indent=3)
        print(json_object)