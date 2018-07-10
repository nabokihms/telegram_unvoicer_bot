from .converters import convert_opus

AUDIO_FILES_TEMPORARY_DIRECTORY = '/tmp'
AUDIO_FILES_LANGUAGE = 'ru-RU'

AUDIO_FILES_CONVERTERS = {
    'opus': convert_opus,
}

AUDIO_FILES_SUPPORTED_FORMATS = frozenset(
    AUDIO_FILES_CONVERTERS
)
