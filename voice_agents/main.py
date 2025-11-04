import speech_recognition as sr
from openai import OpenAI
from system_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
import pyttsx3


load_dotenv()

openai  = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

engine = pyttsx3.init()

def main():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        voice_recognizer.adjust_for_ambient_noise(source)
        voice_recognizer.pause_threshold = 2

        audio = voice_recognizer.listen(source=source)

        text_from_audio = voice_recognizer.recognize_google(audio)

        print('text_from_audio ---', text_from_audio)

        response = openai.chat.completions.create(
            model="gemini-2.5-flash",
            messages=[
                {"role":"system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": text_from_audio}
            ]
        )

        print(response.choices[0].message.content)

        engine.say(response.choices[0].message.content)
        engine.runAndWait()
        
if __name__ == "__main__":
    main()
