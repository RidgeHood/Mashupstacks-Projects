let username= document.querySelector('#name');
let email= document.querySelector('#email');
let password= document.querySelector('#password');
let confirmPass= document.querySelector('#confirm');
let phone= document.querySelector('#phone');

let submit= document.querySelector('#submit');

let minReq=document.querySelector('#minReq');
let minReqEm=document.querySelector('#minReqEm');
let minPass=document.querySelector('#minPass');
let minConfirm=document.querySelector('#minConfirm');
let minPhone=document.querySelector('#minPhone');

let regxName=/[0-9]/;
const regxEmail =/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
let regxPhone=/\D+/;


function allFieldReq(arg,log)
{
    let req= document.querySelector(`.${log} #req`);
  
    if(!arg){
       
       req.classList.add("dinline");
       console.log("cat");
   } 

   else if(arg)
   {
       req.classList.remove("dinline");
       console.log("dog");
   }
}





function minReqFn(min,x)
{   
    
    if(!x){
       
        min.classList.add("dblock");
       
    } 
 
    else if(x)
    {
        min.classList.remove("dblock");
       

    }
    
}



function validation(e){

    e.preventDefault();
    
   allFieldReq(username.value,"logName");
   allFieldReq(email.value,"logEmail");
   allFieldReq(password.value,"logPassword");
   allFieldReq(confirmPass.value,"logConfirm");
   allFieldReq(phone.value,"logPhone");
    
  

     minReqFn(minReqEm,regxEmail.test(email.value));
     minReqFn(minReq,(username.value.length>=3 && regxName.test(username.value)!==true));
     minReqFn(minPhone,(phone.value.length==10 && regxPhone.test(phone.value)!==true));
     minReqFn(minPass,(password.value.length>6));
     minReqFn(minConfirm,(password.value==confirmPass.value));
    
}


submit.addEventListener("click",validation)