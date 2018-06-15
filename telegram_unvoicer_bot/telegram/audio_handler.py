from aiohttp import ClientSession

from telegram_unvoicer_bot.audio import decode_audio, write_file_to_tmp_dir
from telegram_unvoicer_bot.constants import AUDIO_FILES_TEMPORARY_DIRECTORY, \
    TELEGRAM_BOT_FILE_PATH_API_URL, AUDIO_FILES_SUPPORTED_FORMATS
from .abc import AbstractTelegramSupportHandler
from .utils import TelegramApiRequest


class AudioTelegramSupportHandler(AbstractTelegramSupportHandler):

    def __init__(self, session: ClientSession, chat_id: str, file_id: str):
        super().__init__(session, chat_id)
        self._file_id = file_id
        self._downloaded_file_path = None
        self._error_message = None

    async def _get_audio_file_path(self) -> str:
        """
        Getting audio file path from TelegramApi.
        """
        file_data_response = await TelegramApiRequest.get(
            'getFile', data={'file_id': self._file_id}
        )(self._session)

        file_data = await file_data_response.json()
        return file_data['result']['file_path']

    async def _download_audio_file(self):
        """
        Downloading audio file. Return path if downloaded.
        """
        audio_file_path = await self._get_audio_file_path()
        path, ext = audio_file_path.split('.')

        if ext not in AUDIO_FILES_SUPPORTED_FORMATS:
            self._error_message = f'File extension .{ext} is not supported ' \
                                  f'\u2639'
            return

        audio_file_body_resp = await self._session.get(
            f'{TELEGRAM_BOT_FILE_PATH_API_URL}{audio_file_path}'
        )

        if audio_file_body_resp.status != 200:
            self._error_message = u'Download file failed \u2639'
            return

        temp_dir_audio_file_path = \
            f'{AUDIO_FILES_TEMPORARY_DIRECTORY}{audio_file_path}'

        await write_file_to_tmp_dir(
            temp_dir_audio_file_path, await audio_file_body_resp.read()
        )
        self._downloaded_file_path = temp_dir_audio_file_path

    async def handle(self) -> int:

        await self._download_audio_file()

        # If there is a Telegram api error, send error code.
        if self._error_message:
            data = self._error_message
        else:
            data = await decode_audio(self._downloaded_file_path)

        send_message_response = await TelegramApiRequest.post(
            'sendMessage', data={'chat_id': self._chat_id, 'text': data}
        )(self._session)

        return send_message_response.status
