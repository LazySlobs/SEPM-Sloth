from gtts import gTTS
from io import BytesIO
import pygame, settings

def voice_assistant_speak(msg, language=settings.language):
    '''
    Speak the sound using given text

    Parameters:
        msg(str): the text needed to spoken

        Options:
            language(str): the language's short string

    Returns:
        Null
    '''

    # using gtts and bytesio to turn text to audio
    tts = gTTS(text=msg, lang=language)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    # using pygame to play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(fp)
    pygame.mixer.music.play()

    # prevents microphone from listening to the text spoken
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
