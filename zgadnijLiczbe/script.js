//losowanie liczby
var wylosowanaLiczba=Math.floor(Math.random()*100)+1;
//wyswietlanie liczby
function wyborLiczby(){
    var ilosc=document.getElementById("zakres").value;
    document.getElementById("wybranaLiczba").value=ilosc;
    wylosowanaLiczba=Math.floor(Math.random()*ilosc)+1;
    iloscProb=0;
}
//liczba prób
var iloscProb=0
function sprawdzLiczbe(){
    iloscProb++;
    dane=document.getElementById('liczba')
    if(dane.value == wylosowanaLiczba){
        alert("Wygrałeś. Ilość prób to "+iloscProb)
    }else if(dane.value<wylosowanaLiczba){
        alert("Za mała liczba")
    }else{
        alert("Za duża liczba")
    }
}