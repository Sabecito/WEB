function gameRequest(id){
    const URL = 'http://127.0.0.1:5000/juegos-index';
    var data = {};

    if(id === "preguntados-card"){
        data = JSON.stringify({response: "preguntados"});
    }
    else if (id === "snake-card"){
        data = JSON.stringify({response: "snake"});
    }
    else{
        data = JSON.stringify({response: "BLA"});
    }

    fetch(URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: data,
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Success:", data);
        })
        .catch((error) => {
          console.error("Error:", error);
        })
}