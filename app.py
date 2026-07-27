from flask import Flask, render_template, request, jsonify
from agent import correct, explain, rewrite_styles

import speech_recognition as sr
import tempfile

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/grammar')
def grammar():
    return render_template("grammar.html")


@app.route('/speech')
def speech():
    return render_template("speech.html")


@app.route('/check-grammar', methods=['POST'])
def check_grammar():

    data = request.get_json()
    user_input = data.get("text", "").strip()

    if user_input == "":
        return jsonify({
            "original": "",
            "corrected": "",
            "suggestion": "Please enter a sentence.",
            "styles": {
                "professional": "",
                "formal": "",
                "friendly": "",
                "concise": "",
                "advanced": ""
            }
        })

    try:

        corrected = correct(user_input)
        suggestion = explain(user_input, corrected)

        styles = rewrite_styles(corrected)
        
        return jsonify({
            "original": user_input,
            "corrected": corrected,
            "suggestion": suggestion,
            "styles": styles
        })

    except Exception as e:

        return jsonify({
            "original": user_input,
            "corrected": user_input,
            "suggestion": f"Error: {str(e)}",
            "styles": {
                "professional": "",
                "formal": "",
                "friendly": "",
                "concise": "",
                "advanced": ""
            }
        })


@app.route('/analyze-speech', methods=['POST'])
def analyze_speech():

    if 'audio' not in request.files:
        return jsonify({
            "original": "",
            "corrected": "",
            "suggestion": "Please upload an audio file.",
            "styles": {
                "professional": "",
                "formal": "",
                "friendly": "",
                "concise": "",
                "advanced": ""
            }
        })

    audio = request.files['audio']

    if audio.filename == "":
        return jsonify({
            "original": "",
            "corrected": "",
            "suggestion": "No audio file selected.",
            "styles": {
                "professional": "",
                "formal": "",
                "friendly": "",
                "concise": "",
                "advanced": ""
            }
        })

    try:

        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        audio.save(temp.name)
        temp.close()

        recognizer = sr.Recognizer()

        with sr.AudioFile(temp.name) as source:
            audio_data = recognizer.record(source)

        user_input = recognizer.recognize_google(audio_data)

        corrected = correct(user_input)
        suggestion = explain(user_input, corrected)
        styles = rewrite_styles(corrected)

        return jsonify({
            "original": user_input,
            "corrected": corrected,
            "suggestion": suggestion,
            "styles": styles
        })

    except Exception as e:

        return jsonify({
            "original": "",
            "corrected": "",
            "suggestion": f"Error: {str(e)}",
            "styles": {
                "professional": "",
                "formal": "",
                "friendly": "",
                "concise": "",
                "advanced": ""
            }
        })


if __name__ == "__main__":
    app.run(debug=True)