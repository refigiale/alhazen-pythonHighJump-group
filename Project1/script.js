let angka = 0;

document.getElementById("number").textContent = angka;
function pertambahanAngka(){
    angka++
    document.getElementById("number").textContent = angka;
}

function resetAngka(){
    angka = 0;
    document.getElementById("number").textContent = angka;
}



