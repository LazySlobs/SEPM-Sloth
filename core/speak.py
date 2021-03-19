from gtts import gTTS
from io import BytesIO
import pygame

def voice_assistant_speak(msg, language='en'):
    tts = gTTS(text=msg, lang=language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
