function validateForm (){
    let v = document.forms['formLogin']['password'].value;
    if (v == ""){
        alert("Password harus diisi!");
        return false;
    }
}

function changeColor(){
    let color = "red"
    let c = document.getElementById("judul")

    if(judul.style.color != "blue"){
        document.getElementById("judul").style.color = "blue";
        document.getElementById("judul")
        judul.innerHTML="Blue";
        
    }else{
        document.getElementById("judul").style.color = color;
        judul.innerHTML="Red";
    }
}