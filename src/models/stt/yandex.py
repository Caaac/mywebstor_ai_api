import logging
from typing import Optional
from urllib.parse import urlencode
from pydantic import SecretStr

from src.config import settings
from src.utils.stt import STTModel
from src.utils.http_client import HttpClient

class SpeechKit(STTModel):
    api_key: SecretStr = settings.YANDEX_IAM_KEY
    folder_id: Optional[SecretStr] = settings.YANDEX_FOLDER_ID
    url: str = settings.STT_URL_V1

    async def transcript(self, audio: bytes, **params):
        """ 
            Transcribe audio to text.
            Supported PCM format.
        """

        client = HttpClient()
        client.set_headers({
            'Authorization': f'Bearer {self.api_key.get_secret_value()}'
        })
        
        responce = await client.post(
            url=self.path(**params),
            data=audio)
        
        logging.debug(f"[x] SpeechKit | {responce=}")
        
        return responce

    def path(self, **params):
        if self.folder_id:
            params['folderId'] = self.folder_id.get_secret_value()
        return f"{self.url}?{urlencode(params)}"

