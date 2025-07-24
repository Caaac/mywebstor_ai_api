from src.utils.stt import STTModel


class STTService():
    def __init__(self, model: STTModel, **config):
        # self.config = config or {}
        self.model = model

    async def transcribe(self, audio: bytes, **params):
        return await self.model.transcript(audio, **params)
