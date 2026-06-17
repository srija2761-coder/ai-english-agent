from flask import Flask, render_template, request, jsonify
import language_tool_python
import speech_recognition as sr
import tempfile
import os
from speech.speech_to_text import convert_speech

app = Flask(__name__)

# Load Grammar Model
try:
    tool = language_tool_python.LanguageTool('en-US')
except Exception as e:
    print("Error loading grammar tool:", e)
    tool = None


def correct_grammar(text):
    try:
        matches = tool.check(text)
        corrected = language_tool_python.utils.correct(text, matches)
        return corrected, len(matches)
    except Exception as e:
        print(e)
        return text, 0


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/grammar", methods=["POST"])
def grammar():

    try:

        body = request.json
        text = body.get("text")

        if text is None or text == "":
            return jsonify({"error": "No text provided"}), 400

        corrected, mistakes = correct_grammar(text)

        return jsonify({

            "original": text,
            "corrected": corrected,
            "mistakes_found": mistakes

        })

    except Exception as e:
        print(e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/speech", methods=["POST"])
def speech():

    try:

        if "audio" not in request.files:
            return jsonify({"error": "No audio uploaded"}), 400

        file = request.files["audio"]

        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        file.save(temp.name)

        recognizer = sr.Recognizer()

        with sr.AudioFile(temp.name) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        corrected, mistakes = correct_grammar(text)

        os.remove(temp.name)

        return jsonify({

            "speech_text": text,
            "corrected_text": corrected,
            "mistakes_found": mistakes

        })

    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand speech"}), 400

    except sr.RequestError:
        return jsonify({"error": "Speech API unavailable"}), 500

    except Exception as e:
        print(e)
        return jsonify({"error": "Internal Server Error"}), 500


if __name__ == "__main__":
    app.run(debug=True)