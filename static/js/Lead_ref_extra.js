function display(){
   

    var a=document.getElementById('id_lead_ref').value;
    var d=document.getElementById("ip")
    if(isNaN(d)){
        document.getElementById("ip").style.visibility='hidden';
    document.getElementById('id_other').style.visibility='hidden';}
    if(a=="Other"){
        
        document.getElementById('extra').innerHTML='Enter Other info';
        document.getElementById('id_other').style.visibility='visible';
        document.getElementById("ip").style.visibility='visible';
        document.getElementById("ip").required = true;
        
    }
    else if(a=="Social Media"){
        
        document.getElementById('id_other').style.visibility='visible';
        document.getElementById("ip").style.visibility='visible';
        document.getElementById("ip").required = true;
        document.getElementById('extra').innerHTML='Enter name of reference function';
        
    }
    else if(a=="Website"){
        document.getElementById("ip").style.visibility='hidden';
        document.getElementById('id_other').style.visibility='hidden';
        document.getElementById("ip").required = false;   
        

    }
    else if(a=="Marketing"){
        document.getElementById("ip").style.visibility='hidden';
        document.getElementById('id_other').style.visibility='hidden'
        document.getElementById("ip").required = false;
    }
    else{
        document.getElementById("ip").style.visibility='hidden';
        document.getElementById('id_other').style.visibility='hidden';
    }
  
}


function check(){
    var b=document.getElementById('mobile').value;
    if(b==""){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='The number must not contain alphabets';
        document.getElementById('but').style.visibility='hidden';
  
       
    }
    else if(isNaN(b)){
        document.getElementById('al').style.visibility='visible';
         document.getElementById('al').innerHTML='The number must not contain alphabets ';
         document.getElementById('but').style.visibility='hidden';

    }
    else if(b.length<10){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='*The number must contain 10 digits ';
        document.getElementById('but').style.visibility='hidden';
        
    }
    else if(b.length>10){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='The number must contain 10 digits ';
        document.getElementById('but').style.visibility='hidden';
    }
    else{
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').style.visibility='hidden';
        
        document.getElementById('but').style.visibility='visible'; 
    }

    

}
function check2(){
    var c=document.getElementById('mobile1').value;
    if(c==""){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='The number must not contain alphabets';
        document.getElementById('but').style.visibility='hidden';
  
       
    }
    else if(isNaN(c)){
        document.getElementById('al').style.visibility='visible';
         document.getElementById('al').innerHTML='The number must not contain alphabets ';
         document.getElementById('but').style.visibility='hidden';

    }
    else if(c.length<10){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='*The number must contain 10 digits ';
        document.getElementById('but').style.visibility='hidden';
        
    }
    else if(c.length>10){
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').innerHTML='The number must contain 10 digits ';
        document.getElementById('but').style.visibility='hidden';
    }
    else{
        document.getElementById('al').style.visibility='visible';
        document.getElementById('al').style.visibility='hidden';
        
        document.getElementById('but').style.visibility='visible'; 
    }
}