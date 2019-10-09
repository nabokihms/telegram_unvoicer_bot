from aiohttp import ClientSession

from telegram_unvoicer_bot.audio import decode_audio, write_file_to_tmp_dir, \
    AUDIO_FILES_SUPPORTED_FORMATS, AUDIO_FILES_TEMPORARY_DIRECTORY
from telegram_unvoicer_bot.telegram.const import TELEGRAM_BOT_FILE_PATH_API_URL

from .abc import AbstractTelegramSupportHandler
from .request import telegram_api_get_file_method, \
    telegram_api_send_message


class AudioTelegramSupportHandler(AbstractTelegramSupportHandler):
    """
    Additional hendler for Telegram bot.
    """
    def __init__(self, session: ClientSession, chat_id: str, file_id: str):
        super().__init__(session, chat_id)
        self._file_id = file_id
        self._downloaded_file_path = None
        self._error_message = None

    async def _get_audio_file_path(self) -> str:
        file_data_response = await telegram_api_get_file_method(
            self._session, data={'file_id': self._file_id}
        )
        file_data = await file_data_response.json()
        return file_data['result']['file_path']

    async def _download_audio_file(self):
        audio_file_path = await self._get_audio_file_path()
        path, ext = audio_file_path.split('.')

        if ext not in AUDIO_FILES_SUPPORTED_FORMATS:
            self._error_message = f'File extension .{ext} not supported.' \
                                  f'\u2639'
            return

        audio_file_body_resp = await self._session.get(
            f'{TELEGRAM_BOT_FILE_PATH_API_URL}{audio_file_path}'
        )

        if audio_file_body_resp.status != 200:
            self._error_message = u'Unable to download the file \u2639'
            return

        temp_dir_audio_file_path = \
            f'{AUDIO_FILES_TEMPORARY_DIRECTORY}/{audio_file_path}'

        await write_file_to_tmp_dir(
            temp_dir_audio_file_path, await audio_file_body_resp.read()
        )
        self._downloaded_file_path = temp_dir_audio_file_path

    async def handle(self) -> int:

        await self._download_audio_file()
        try:
            if self._error_message:
                data = self._error_message
            else:
                data = await decode_audio(self._downloaded_file_path)
        except Exception:
            data = 'Unable to decode message to text \u2639'

        send_message_response = await telegram_api_send_message(
            self._session, data={'chat_id': self._chat_id, 'text': data}
        )

        return send_message_response.status
