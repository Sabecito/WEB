var clicksCounter = 0;

function cbChange(obj){
    var cbs = document.getElementsByClassName("cb");
    for (var i = 0; i < cbs.length; i++) {
        cbs[i].checked = false;
    }
    obj.checked = true;
}

function setOptionsText(){
    //var data = {{ data|tojson|safe}};
    
    document.getElementById("questionText").textContent = "HOLO";
    document.getElementById("firstOptionText").textContent = "First option to choose!";
    //document.getElementById("secondOptionText").textContent = "Second option to choose!";
    //document.getElementById("thirdOptionText").textContent = "Third option to choose!";
    //document.getElementById("fourthOptionText").textContent = "Fourth option to choose!";
}

function fetchObjetcChecked(){
    const URL = 'http://127.0.0.1:5000/answersGame';
    var data = {}
    
    clicksCounter+=1;
    if(document.getElementById("firstCheckbox").checked){
        data = {response: 1}    
    }else if (document.getElementById("secondCheckbox").checked){
        data = {response: 2}   
    }else if(document.getElementById("thirdCheckbox").checked){
        data = {response: 3}   
    }else{
        data = {response: 4}   
    }

    /*EN ESTE PUNTO DEBERIA IR GUARDANDO LAS RESPUESTAS PARA LUEGO MANDARLAS EN UNA LISTA Y HACER SOLO UN POST*/

    fetch(URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then(window.location.href = "http://127.0.0.1:5000/juegos-index")
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
        })
        .catch((error) => {
          console.error("Error:", error);
        })
    }
    //if(clicksCounter >= 5){
        
//}