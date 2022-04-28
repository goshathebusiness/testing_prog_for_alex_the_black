5252

for (var i=0;i<q_num;i++){
  let name="answer_for_question"+String(i);
   q_all=document.getElementsByName(name)
   console.log(document.getElementsByName(name).value)
   result_value=parseInt(document.getElementsByName(name).value)
   final_value=final_value+result_value;
 }