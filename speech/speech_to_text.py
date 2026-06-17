import speech_recognition as sr


def convert_speech(audio_path):

    recognizer = sr.Recognizer()

    try:

        with sr.AudioFile(audio_path) as source:

            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)

        return text

    except sr.UnknownValueError:

        return "Could not understand audio."

    except sr.RequestError:

        return "Speech recognition service unavailable."

    except Exception as e:

        return str(e)