import os
import uvicorn
from src.routers.translate import router as translate_router

from fastapi import FastAPI, Request, Response

class App:

  def __init__(self):
    self.app = FastAPI()
    
    @self.app.middleware("http")
    async def verify_api_key(request: Request, call_next):
      valid_api_key = self._get_valid_api_key()
      if not valid_api_key:
        return await call_next(request)
      api_key = request.headers.get("x-api-key")
      if not api_key:
        return Response(content="Missing API Key", status_code=401)
      if api_key != valid_api_key:
        return Response(content="Invalid API Key", status_code=403)
      return await call_next(request)

    self.app.include_router(translate_router)

  def run(self):
    uvicorn.run(self.app, host="0.0.0.0", port=8000)
  
  def _get_valid_api_key(self):
    return os.environ.get("API_KEY")
