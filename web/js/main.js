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