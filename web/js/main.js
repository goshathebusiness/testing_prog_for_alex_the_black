async function grade() {
  num_true = document.getElementById('1').value;
  let num_true_p = await eel.count_true(num_true)();
  document.getElementById('grade').value = num_true_p;
  eel.count_true(num_true)
}
document.getElementById("grade").onclick = run();

document.querySelector('value=1')
