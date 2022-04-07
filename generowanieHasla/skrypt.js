var iloscZn=8;
var iloscCyfr=0;

function iloscZnakow(){
    iloscZn=document.getElementById("iloscZnakow").value;
    document.getElementById("iloscCyfr").max=+iloscZn;
    document.getElementById("iloscMaleL").max=+iloscZn;
}

function wybCyfr(){
    iloscCyfr=document.getElementById("iloscCyfr").value;
    document.getElementById("wybCyfr").value=iloscCyfr;
}
function wybMaleL(){
    iloscCyfr=document.getElementById("iloscMaleL").value;
    document.getElementById("wybMaleL").value=iloscCyfr;
}