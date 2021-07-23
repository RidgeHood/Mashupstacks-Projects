click=document.querySelector("#click");
dropdown=document.querySelector("#dropdown");
x=document.querySelector("#x");
y=document.querySelector("#y");
result=document.querySelector("#result");
let ans=0;


function calc(e)
{
  if(dropdown.value=="+")
  {
      ans=parseInt(x.value)+parseInt(y.value);
    }
  else if(dropdown.value=="-")
  {
      ans=parseInt(x.value)-parseInt(y.value);
    }
   else if(dropdown.value=="*")
    {ans=parseInt(x.value)*parseInt(y.value);}
    else if(dropdown.value=="/")
    {ans=parseInt(x.value)/parseInt(y.value);}
    console.log(ans);


    result.innerText=ans;

}


click.addEventListener("click",calc);parseInt