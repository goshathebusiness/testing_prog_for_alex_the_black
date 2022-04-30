let q_num=3;
let selectedValue=0;

//submit_button.onclick=function(){
//  for (var i=0;i<=q_num;i++){
//   let name="answer_for_question"+String(i);
//   if (document.getElementById.checked){
//     selectedValue=document.getElementsByName(name).value;
//     console.log(selectedValue)
//   }
//   document.getElementById("submit_button").innerHTML=("vash result")+selectedValue;
//  }
//}

submit_button.onclick=function(){
  let final_value;
  for (var i=0;i<=q_num;i++){
   let name="answer_for_question"+String(i);
   answers=document.getElementsByName(name).value;
   console.log(answers)
   let answers_value, answers_checked;
   answers_checked=answers.checked;
   console.log(answers_checked.value);
   console.log(answers_value)
   for (let j=0;j<=answers;j++){
     ;
     answers_value=answers_value+answers_checked[j];
     console.log(answers_value)
   }
  console.log(final_value);
  document.getElementById("result").innerHTML="Vash result "+final_value;
  }
}