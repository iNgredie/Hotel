from fastapi import FastAPI

from .api import router

app = FastAPI(
    title='Hotel',
    desctiption='Приложение для функционирования отеля',
    version='0.0.1'
)


app.include_router(router)
