var iloscZn=8;
var iloscCyfr=0;
var iloscMaleL=0;
var iloscWolnychZn=0;
var iloscDuzeL=0;
var iloscSpec=0;

function iloscZnakow(){
    iloscZn=document.getElementById("iloscZnakow").value;
    
    ustawWolne();
}

function wybCyfr(){
    iloscCyfr=document.getElementById("iloscCyfr").value;
    document.getElementById("wybCyfr").value=iloscCyfr;
    ustawWolne();
}
function wybMaleL(){
    iloscMaleL=document.getElementById("iloscMaleL").value;
    document.getElementById("wybMaleL").value=iloscMaleL;
    ustawWolne();
}
function wybDuzeL(){
    iloscDuzeL=document.getElementById("iloscDuzeL").value;
    document.getElementById("wybDuzeL").value=iloscDuzeL;
    ustawWolne();
}
function wybSpec(){
    iloscSpec=document.getElementById("iloscSpec").value;
    document.getElementById("wybSpec").value=iloscSpec;
    ustawWolne();
}
function ustawWolne(){
    iloscWolnychZn=+iloscZn-(+iloscCyfr+ +iloscMaleL+ +iloscDuzeL+ +iloscSpec);
    document.getElementById("wynik").value=iloscWolnychZn;
    document.getElementById("iloscCyfr").max=+iloscCyfr+ +iloscWolnychZn;
    document.getElementById("iloscMaleL").max=+iloscMaleL+ +iloscWolnychZn;
    document.getElementById("iloscDuzeL").max=+iloscDuzeL+ +iloscWolnychZn;
    document.getElementById("iloscSpec").max=+iloscSpec+ +iloscWolnychZn;
}