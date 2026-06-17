// Grammar Checker

async function checkGrammar() {

    const text = document.getElementById("text").value;

    if (text.trim() === "") {
        alert("Please enter some text.");
        return;
    }

    try {

        const response = await fetch("/grammar", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                text: text
            })

        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("original").innerText =
            data.original;

        document.getElementById("corrected").innerText =
            data.corrected;

        document.getElementById("mistakes").innerText =
            data.mistakes_found;

    }

    catch (error) {

        console.log(error);
        alert("Server Error");

    }

}



// Speech Analyzer

async function uploadAudio() {

    const audio = document.getElementById("audio").files[0];

    if (!audio) {
        alert("Please select an audio file.");
        return;
    }

    const formData = new FormData();

    formData.append("audio", audio);

    try {

        const response = await fetch("/speech", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("original").innerText =
            data.speech_text;

        document.getElementById("corrected").innerText =
            data.corrected_text;

        document.getElementById("mistakes").innerText =
            data.mistakes_found;

    }

    catch (error) {

        console.log(error);
        alert("Server Error");

    }

}