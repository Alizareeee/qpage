var a="QPAGE Version 1.8 : \n\n + Meta File\n + Error And Warning Handler";

function message(){
    alert(a);
    
}

function httpGet()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "http://sepkjaer.pythonanywhere.com/download", false );
    xmlHttp.send( null );
}
function func1(w){
    var b=document.getElementsByTagName("body");
    if (w==1){
        b[0].style.background="linear-gradient(black,white)";
    }
    else if (w==2){
        b[0].style.background="linear-gradient(red,white)";
    }
    else if (w==3){
        b[0].style.background="linear-gradient(pink,white)";
    }
    else if (w==5){
        b[0].style.background="linear-gradient(green,white)";
    }
    else if (w==6){
        b[0].style.background="linear-gradient(blue,white)";
    }
    else{
        b[0].style.background="linear-gradient(orange,white)";
    }
    
}