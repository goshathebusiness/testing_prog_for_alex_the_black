async function count() {
  //let len_q = await eel.CountQuestions()();
  len_q=12
  score=0
  arr=document.querySelectorAll("input[type='radio']:checked");
  arr.forEach(element => {
    score=score+parseInt(element.value)
  });
  document.getElementById('result').innerHTML='Результат тесту: '+score+'/'+len_q;
}

function block(){
  arr_d=document.querySelectorAll("input[type='radio']");
  arr_d.forEach(element => {
    element.disabled='True';
  });
}