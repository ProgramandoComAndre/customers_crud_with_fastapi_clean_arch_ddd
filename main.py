from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import JSONResponse
from enum import Enum
from typing import Dict, List, Annotated
from random import randint
from pydantic import BaseModel
from json import JSONEncoder
from routers import CustomerRouter

app = FastAPI()

app.include_router(CustomerRouter)

@app.exception_handler(KeyError)
async def bad_request(request, exc):
    return JSONResponse({"error": str(exc)}, status_code=400)