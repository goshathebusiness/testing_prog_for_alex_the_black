function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

let q_num=3, result_value=0;

submit_button2.onclick=function(){
  cheked_value=document.querySelector('input[type="radio"]:checked').value;

  result_value=result_value+cheked_value
  document.getElementById("result").innerHTML=result_value
}

//if(document.getElementById('summer').checked) {   
//  var selectedValue = document.getElementById('summer').value;  
//  alert("Selected Radio Button is: " + selectedValue);    
//}  
let final_value=0;
submit_button1.onclick=function(){
  for (var i=0;i<q_num;i++){
   let name="answer_for_question"+String(i);
    result_value=parseInt(document.getElementsByName(name).value)
    final_value=final_value+result_value;
  }
  console.log(final_value);
  document.getElementById("result").innerHTML="Vash result "+final_value;
}