from enum import Enum


class AudioFormat(str, Enum):
    """
        Supported audio formats
        https://yandex.cloud/ru/docs/speechkit/stt/api/request-api
    """
    lpcm = 'lpcm'
    ogg = 'oggopus'


class AudioLanguage(str, Enum):
    """
        Supported languages
        https://yandex.cloud/ru/docs/speechkit/stt/models
    """
    auto = 'auto'
    ru = 'ru-RU'
    en = 'en-US'
    de = 'de-DE'
    kz = 'kk-KZ'


class AudioTopic(str, Enum):
    """
        Supported topics
        https://yandex.cloud/ru/docs/speechkit/stt/models
    """
    general = 'general'
    test = 'general:rc'
    previous = 'general:deprecated'
