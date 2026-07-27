function openGrammar() {
    window.location.href = "/grammar";
}

function openSpeech() {
    window.location.href = "/speech";
}

function checkGrammar() {

    let text = document.getElementById("grammarInput").value.trim();

    if (text === "") {
        alert("Please enter a sentence.");
        return;
    }

    fetch("/check-grammar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {

        // Debugging
        console.log("Response from Flask:");
        console.log(data);

        document.getElementById("originalText").innerText =
            data.original || "";

        document.getElementById("correctedText").innerText =
            data.corrected || "";

        document.getElementById("aiSuggestion").innerText =
            data.suggestion || "";

        if (data.styles) {

            console.log("Styles:");
            console.log(data.styles);

            document.getElementById("professional").innerText =
                data.styles.professional || "";

            document.getElementById("formal").innerText =
                data.styles.formal || "";

            document.getElementById("friendly").innerText =
                data.styles.friendly || "";

            document.getElementById("concise").innerText =
                data.styles.concise || "";

            document.getElementById("advanced").innerText =
                data.styles.advanced || "";

        } else {

            console.log("No styles received!");

            document.getElementById("professional").innerText = "";
            document.getElementById("formal").innerText = "";
            document.getElementById("friendly").innerText = "";
            document.getElementById("concise").innerText = "";
            document.getElementById("advanced").innerText = "";
        }

    })
    .catch(error => {
        console.error(error);
        alert("Something went wrong!");
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

        console.log("Speech Response:");
        console.log(data);

        document.getElementById("originalText").innerText =
            data.original || "";

        document.getElementById("correctedText").innerText =
            data.corrected || "";

        document.getElementById("aiSuggestion").innerText =
            data.suggestion || "";

        if (data.styles) {

            document.getElementById("professional").innerText =
                data.styles.professional || "";

            document.getElementById("formal").innerText =
                data.styles.formal || "";

            document.getElementById("friendly").innerText =
                data.styles.friendly || "";

            document.getElementById("concise").innerText =
                data.styles.concise || "";

            document.getElementById("advanced").innerText =
                data.styles.advanced || "";

        }

    })
    .catch(error => {
        console.error(error);
        alert("Something went wrong!");
    });
}