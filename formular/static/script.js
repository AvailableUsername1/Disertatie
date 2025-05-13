function getRandomValue(min, max) {
    // Generate a random decimal between 0 and 1
    var randomDecimal = Math.random();
  
    // Scale and shift the random decimal to fit within the desired range
    var randomValue = min + randomDecimal * (max - min);
  
    // Round the result to an integer if needed
    // randomValue = Math.round(randomValue);
  
    return randomValue;
  }

function aiButtonClick(aiWait, number, lang) {
    aiButton = document.getElementById('ai_button');
    aiLoader = document.getElementById('ailoader');
    var prediction = document.createElement('h2');
    var number = parseInt(number);
    if (number === 2) {
        if (lang === "eng") {
            prediction.textContent = "AI prediction: Grade I";
        } else if (lang === "ro") {
            prediction.textContent = "Predicție IA: Grad I";
        } else {
            prediction.textContent = "KI-Vorhersage: Grad I";
        }
    } else if (number === 1 || number === 4 || number === 8) {
        if (lang === "eng") {
            prediction.textContent = "AI prediction: Grade II";
        } else if (lang === "ro") {
            prediction.textContent = "Predicție IA: Grad II";
        } else {
            prediction.textContent = "KI-Vorhersage: Grad II";
        }
    } else if (number === 3 || number === 7 || number === 9 || number === 5 || number === 10) {
        if (lang === "eng") {
            prediction.textContent = "AI prediction: Grade III";
        } else if (lang === "ro") {
            prediction.textContent = "Predicție IA: Grad III";
        } else {
            prediction.textContent = "KI-Vorhersage: Grad III";
        }
    } else {
        if (lang === "eng") {
            prediction.textContent = "AI prediction: Grade IV";
        } else if (lang === "ro") {
            prediction.textContent = "Predicție IA: Grad IV";
        } else {
            prediction.textContent = "KI-Vorhersage: Grad IV";
        }
    }
    nextbutton = document.getElementById('nextbutton');

    if (aiButton) {
        aiButton.style.display = "none";
        ailoader.style.display = "block";
        setTimeout(function(){
            ailoader.style.display = "none";
            document.getElementById('prediction').appendChild(prediction);
            nextbutton.classList.remove('d-none');
        }, aiWait)
    }
}

document.getElementById("showInfo").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "flex";
});

document.getElementById("closeButton").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "none";
});