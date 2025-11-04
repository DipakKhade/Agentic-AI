import speech_recognition as sr

def main():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        voice_recognizer.pause_threshold(2)

        audio = voice_recognizer.listen(source=source)


if __name__ == "__main__":
    main()
