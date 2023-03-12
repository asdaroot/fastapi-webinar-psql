from fastapi import FastAPI
from app.handlers import router

def get_application() -> FastAPI:
    application = FastAPI()              #создаем объеки из экземпляра класса
    application.include_router(router)   #добавить роутер
    return application                   #возвращаем объект


app = get_application()