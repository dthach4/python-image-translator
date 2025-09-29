import uvicorn
from src.routers.translate import router as translate_router

from fastapi import FastAPI

class App:

  def __init__(self):
    self.app = FastAPI()
    self.app.include_router(translate_router)

  def run(self):
    uvicorn.run(self.app, host="0.0.0.0", port=8000)