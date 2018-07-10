import asyncio
import subprocess

import speech_recognition as sr

from .const import AUDIO_FILES_CONVERTERS, \
    AUDIO_FILES_LANGUAGE
from .utils import delete_file_from_tmp_dir

__all__ = [
    'decode_audio',
]

_DECODE_MAX_LENGTH: int = 90


# todo: избавиться от использования библиотеки
def _google_speech_recognise(file_path: str) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = r.record(source)
        return r.recognize_google(audio, language=AUDIO_FILES_LANGUAGE)


async def decode_audio(file_path: str) -> str:
    path, ext = file_path.split('.')

    new_file_path = f'{path}.wav'
    await AUDIO_FILES_CONVERTERS[ext](file_path, new_file_path)

    # todo: декодировать длинные аудиофайлы чанками
    seconds = float(
        subprocess.check_output([
            'soxi', '-D', new_file_path
        ]).decode().strip()
    )

    if seconds > _DECODE_MAX_LENGTH:
        return f'Длина файла составляет {seconds} секунды! ' \
               f'Я не умею декодировать настолько большие \U0001f605'

    text = _google_speech_recognise(new_file_path)

    await asyncio.wait([
        delete_file_from_tmp_dir(x) for x in (file_path, new_file_path)
    ])
    return text
