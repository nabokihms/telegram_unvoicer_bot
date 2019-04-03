from .converters import convert_opus

__all__ = [
    'AUDIO_FILES_TEMPORARY_DIRECTORY',
    'AUDIO_FILES_LANGUAGE',
    'AUDIO_FILES_CONVERTERS',
    'AUDIO_FILES_SUPPORTED_FORMATS',
]


AUDIO_FILES_TEMPORARY_DIRECTORY = '/tmp'
AUDIO_FILES_LANGUAGE = 'ru-RU'

AUDIO_FILES_CONVERTERS = {
    'opus': convert_opus,
    'oga': convert_opus,
}

AUDIO_FILES_SUPPORTED_FORMATS = frozenset(
    AUDIO_FILES_CONVERTERS
)
