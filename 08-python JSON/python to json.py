#menggunakan package json
import json


#object python tipe data structure dictionary

data = {
    "siswa":[
        {
            "nama":"Refina",
            "umur" :"19"
        },
        {
            "nama":"Akmal",
            "umur" :"12"
        },
        {
            "nama":"Pandu",
            "umur" :"12"
        },
        {
            "nama":"Dino",
            "umur" :"12"
        }
    ]

}

print(type(data)) #dict


with open("data_file_biasa.json", "w") as file: #membuat file dengan nama "data_file.json" yang berisi data oobject python
    json.dump(data, file) #json.dump convert dari object python data menjadi json file

with open("data_file.json", "w") as file: #membuat file dengan nama "data_file.json" yang berisi data oobject python
    json.dump(data, file, indent=4) #json.dump convert dari object python data menjadi json file
    #indent itu digunakan agar datanya beautify (rapih)

    
#jika mau digunakan lagi bisa pake script di bawah ini 
print(json.dumps(data)) #menampilkan json object di terminal vscod

