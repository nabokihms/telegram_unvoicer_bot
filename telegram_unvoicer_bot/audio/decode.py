import subprocess

import speech_recognition as sr

from telegram_unvoicer_bot.constants import AUDIO_FILES_CONVERTERS, \
    AUDIO_FILES_LANGUAGE

__all__ = [
    'decode_audio',
]

_DECODE_MAX_LENGTH = 90


# todo: get rid of speech_recognition library
def _google_speech_recognise(file_path: str):
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        return r.recognize_google(audio, language=AUDIO_FILES_LANGUAGE)


async def decode_audio(file_path: str) -> str:
    """
    Main method to decode audio files.
    """
    path, ext = file_path.split('.')

    new_file_path = f'{path}.wav'
    await AUDIO_FILES_CONVERTERS[ext](file_path, new_file_path)

    # todo: decode big files by chunks
    seconds = float(subprocess.check_output([
        'soxi',
        '-D',
        new_file_path
    ]).decode().strip())

    if seconds > _DECODE_MAX_LENGTH:
        return f'Length of your file is {seconds} seconds! ' \
               f'I can\'t decode that big now \U0001f605'

    return _google_speech_recognise(new_file_path)
