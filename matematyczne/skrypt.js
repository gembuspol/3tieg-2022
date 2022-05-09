function euklides(){
    let liczbaA=parseInt(document.getElementById("liczbaA").value)
    let liczbaB=parseInt(document.getElementById("liczbaB").value)
    while(liczbaA!==liczbaB){
        if(liczbaA>liczbaB){
            liczbaA=liczbaA-liczbaB
        }else{
            liczbaB=liczbaB-liczbaA
        }
    }
    document.getElementById("euklidesWynik").value=liczbaA
}
function euklides2(liczbaA,liczbaB){
    while(liczbaA!==liczbaB){
        if(liczbaA>liczbaB){
            liczbaA=liczbaA-liczbaB
        }else{
            liczbaB=liczbaB-liczbaA
        }
    }
    return liczbaA
}
function NWW(){
    
}