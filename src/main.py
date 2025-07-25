import os
import uvicorn
import logging

from fastapi import FastAPI
from datetime import datetime

from src.config import settings
from src.api import api_router

# Logger
os.makedirs('./logs', exist_ok=True)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(
            f'./logs/{datetime.now().strftime("%Y-%m-%d")}.log'),
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)

app = FastAPI(
    version=settings.VERSION,
    docs_url='/docs',
    openapi_url='/openapi.json',
    redoc_url='/redoc',
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Local development"
        }
    ]
)
app.include_router(api_router, prefix="/api")


def main():
    uvicorn.run("src.main:app", host="0.0.0.0",
                port=8000, reload=settings.DEBUG, log_config=None)


if __name__ == '__main__':
    main()
