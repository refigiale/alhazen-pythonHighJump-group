let cuaca = "cerah";

if (cuaca=="hujan"){
    console.log("Bawa payung")
}else{
    console.log("Tidak perlu membawa payung")
}


// let number = prompt("Masukkan angka: ")
// if (number %2 == 0){//habis dibagi 2 atau sisa hasil baginya 0
//     alert("Angka " + number + " merupakan bilangan genap")
// }else{
//     alert("Agka " + number + " merupakan bilangan ganjil")
// }



// score = prompt("Masukkan angka yang kamu punya: ")
// modulus = score % 2
// switch(modulus){
//     case 0:
//         alert(score + " adalah bilangan genap")
//     case 1:
//         alert(score + " adalah bilangan ganjil")
// }

cuaca = prompt("Bagaimana cuaca hari ini? cerah/hujan");
switch(cuaca){
    case "hujan":
        alert("Aduh bawa payung!")
    case "cerah":
        alert("Wah have a nice day kalo cerah!")
}   
