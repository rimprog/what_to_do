import httpx
from openai import AsyncOpenAI, DefaultAsyncHttpxClient

from app.config import settings


class OpenAIConnector:

    def __init__(self) -> None:
        self.proxy_mounts = {
            "http://": httpx.AsyncHTTPTransport(proxy=settings.PROXY),
            "https://": httpx.AsyncHTTPTransport(proxy=settings.PROXY),
        }
        self.client = AsyncOpenAI(
            api_key=settings.OPEN_AI_API_KEY,
            http_client=DefaultAsyncHttpxClient(
                mounts=self.proxy_mounts,
            )
        )

    async def generate_text(self, prompt: str, model: str = "gpt-3.5-turbo", temperature: float = 1.2) -> str:
        chat_completion = await self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
            temperature=temperature
        )

        text = chat_completion.choices[0].message.content

        return text
