import speech_recognition as sr
from core.listen import record_audio
from core.speak import voice_assistant_speak
from core.proccess_respond import respond
import settings

settings.init()

r1 = sr.Recognizer() # create a recognizer object to recognize texts
# r1.energy_threshold = settings.energy_threshold 
r2 = sr.Recognizer() # create a recognizer object to respond
# r2.energy_threshold = settings.energy_threshold 

WAKE = "wake up"

def main():
    wake = False
    while True:
        # speak if the ask variable is a string
        with sr.Microphone() as source:
            # adjust for ambient noise
            print("Calibrating...")
            r1.adjust_for_ambient_noise(source, duration=1)
            r1.energy_threshold += 250

            # starts to listen for keyword
            print("Listening for keyword...")
            audio = r1.listen(source)
            listen_for_keyword = ""
            try:
                listen_for_keyword = r1.recognize_google(audio)
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                voice_assistant_speak("Sorry, my speech service is down")
                continue
            except:
                print("Something went wrong.")
                continue
            print("listen_for_keyword = " + listen_for_keyword)

            # keyword heard, wake up the voice assistant
            if listen_for_keyword.count(WAKE) > 0:
                wake = True
                print("Sloth is awake...")
                voice_assistant_speak("How can I help you?")

                if (wake):
                    while True:
                        # listen to users
                        voice_data, language = record_audio(r1)
                        # if user tells program to stop
                        if voice_data.lower() == "go to sleep" or voice_data.lower() == "go back to sleep":
                            wake = False
                            break
                        print("Voice data: " + voice_data)  # print user's voice data
                        respond(r2, voice_data, language=language)  # respond to user's voice data
            elif listen_for_keyword.lower() == "stop the program":
                break

if __name__ == '__main__':
    main()
