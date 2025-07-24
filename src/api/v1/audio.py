import base64
import logging
from fastapi import APIRouter, Request

from src.services.stt import STTService
from src.models.stt.yandex import SpeechKit
from src.schemas.api.v1 import SAudioTranscript

router = APIRouter()


@router.post('/test')
async def test(request: SAudioTranscript):
    service = STTService(model=SpeechKit())
    result = await service.transcribe(request.audio, **request.params.model_dump())
    logging.info(f'FINISH | {result=}')
    return result


@router.post('/transcript')
async def test(request: SAudioTranscript):
    service = STTService(model=SpeechKit())
    result = await service.transcribe(request.audio, **request.params.model_dump())
    logging.info(f'FINISH | {result=}')
    return result
