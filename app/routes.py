from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

from app.models import RecommendationRequest
from utils.openai_connector import OpenAIConnector

# Инициализация шаблонов
templates = Jinja2Templates(directory="app/templates")

# Создание маршрутизатора
router = APIRouter()

# Инициализация OpenAIConnector с использованием настроек
openai_connector = OpenAIConnector()

@router.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/get_recommendation", response_class=JSONResponse)
async def get_recommendation(request: RecommendationRequest):
    prompt = f"Сгенерируй рандомную затравку для себя, чтобы каждая даваемая рекомендация была уникальна. Опираясь на сгенерированную затравку, дай рекомендацию для {request.gender}, возраст: {request.age}, тип активности: {request.activity}, настроение: {request.mood}, бюджет: {request.budget}. Важно! В ответ выводи только рекомендацию, скрой затравку."

    # Асинхронный вызов ChatGPT API
    chatgpt_recommendation = await openai_connector.generate_text(prompt)

    # Возвращаем рекомендацию в JSON формате для отображения на клиенте
    return {"recommendation": chatgpt_recommendation}
