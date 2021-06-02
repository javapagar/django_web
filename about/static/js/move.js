
var arrow = document.getElementById("arrow")

while(true){
    if ( arrow.getAttribute("data-fa-transform") == "shrink-8 down-10"){
        arrow.setAttribute("data-fa-transform","shrink-8 up-10")
    }else{
        arrow.setAttribute("data-fa-transform","shrink-8 down-10")
    }
    
}