from typing import Dict, FrozenSet, Callable

from ..audio import convert_opus

AUDIO_FILES_TEMPORARY_DIRECTORY: str = '/tmp/'
AUDIO_FILES_LANGUAGE: str = 'ru-RU'

AUDIO_FILES_CONVERTERS: Dict[str, Callable] = {
    'opus': convert_opus,
}

AUDIO_FILES_SUPPORTED_FORMATS: FrozenSet[str] = frozenset(
    AUDIO_FILES_CONVERTERS
)
