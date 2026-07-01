
function openGrammar() {
    window.location.href = "/grammar";
}

function openSpeech() {
    window.location.href = "/speech";
}


function checkGrammar() {
    let text = document.getElementById("grammarInput").value;

    fetch("/check-grammar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {

        document.getElementById("originalText").innerText =
            data.original;

        document.getElementById("correctedText").innerText =
            data.corrected;

        document.getElementById("aiSuggestion").innerText =
            data.suggestion;

    })
    .catch(err => {
        console.error(err);
        alert("Something went wrong");
    });
}


function analyzeSpeech() {

    let fileInput = document.getElementById("audioInput");

    if (!fileInput.files.length) {
        alert("Please upload an audio file!");
        return;
    }

    let formData = new FormData();
    formData.append("audio", fileInput.files[0]);

    fetch("/analyze-speech", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        document.getElementById("originalText").innerText =
            data.original;

        document.getElementById("correctedText").innerText =
            data.corrected;

        document.getElementById("aiSuggestion").innerText =
            data.suggestion;

    })
    .catch(error => {
        console.error(error);
        alert("Something went wrong!");
    });

}