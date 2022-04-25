db = openDatabase("/QAdb.db", "0.1", "A list of to do items.", 200000);
if(!db){alert("Failed to connect to database.");}

document.getElementById("button-name").addEventListener("click", ()=>{eel.settings()}, false);
document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

$('#addDynamicExtraFieldButton').click(function(event) {
  addDynamicExtraField();
  return false;
});

function addDynamicExtraField() {
      var div = $('<div/>', {
          'class': 'DynamicExtraField'
      }).appendTo($('#DynamicExtraFieldsContainer'));
      var br = $('<br/>').appendTo(div);
      var label = $('<label/>').html("Доп. поле ").appendTo(div);
      var input = $('<input/>', {
          value: 'Удаление',
          type: 'button',
          'class': 'DeleteDynamicExtraField'
      }).appendTo(div);
      input.click(function() {
          $(this).parent().remove();
      });
      var br = $('<br/>').appendTo(div);
      var textarea = $('<textarea/>', {
          name: 'DynamicExtraField[]',
          cols: '50',
          rows: '3'
      }).appendTo(div);
  }
//Для удаления первого поля. если оно не динамическое
$('.DeleteDynamicExtraField').click(function(event) {
  $(this).parent().remove();
  return false;
});