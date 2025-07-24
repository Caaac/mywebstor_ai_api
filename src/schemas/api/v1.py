from typing import Optional
from pydantic import BaseModel, ConfigDict, Field, Base64Bytes, field_validator
from src.enums import AudioFormat, AudioLanguage, AudioTopic


class SAudioTranscriptParams(BaseModel):    
    sampleRateHertz: Optional[int] = None
    topic: AudioTopic = Field(default=AudioTopic.general, validate_default=True)
    format: AudioFormat = Field(default=AudioFormat.ogg, validate_default=True)
    lang: AudioLanguage = Field(default=AudioLanguage.auto, validate_default=True)
    bits: int
    
    model_config = ConfigDict(use_enum_values=True)

    @field_validator('sampleRateHertz')
    def validator_sampleRateHertz(cls, value):
        if value not in (8000, 16000, 48000):
            raise ValueError('sampleRateHertz must be 8000, 16000, or 48000')
        return value

    @field_validator('bits')
    def validator_bits(cls, value):
        if value not in {16}:
            raise ValueError('bits must be 16')
        return value


class SAudioTranscript(BaseModel):
    audio: Base64Bytes
    params: SAudioTranscriptParams
