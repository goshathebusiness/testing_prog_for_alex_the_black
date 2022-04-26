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

let newDog = document.createElement('div')

 newDog.classList.add('dog')

 const myImage = document.createElement('img')
 myImage.src="https://picsum.photos/id/237/500/500";
 myImage.alt='Dog photo'

 const h2 = document.createElement('h2')
 h2.textContent = 'My name is Roviel and i love playing and eating.'

 const p = document.createElement('p')
 p.classList.add('moreInfo')

 p.textContent= 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat.'


 const button = document.createElement('button')
 button.classList.add('btn')
 button.textContent= 'Click to read  more about me '

 document.body.appendChild(newDog)
 newDog.appendChild(myImage)
 newDog.appendChild(h2)
 newDog.appendChild(p)
 newDog.appendChild(button)

// Добавление обработчиков событий

 function showMore(){
   document.querySelector('.moreInfo').style.display ='block'
}

document.querySelector('.btn').addEventListener('click', showMore)

const form = document.getElementById('test');
form.elements["1"];
let formTrue = form.value;

form.addEventListener("submit",(event)=>{
  event.preventDefault();
});