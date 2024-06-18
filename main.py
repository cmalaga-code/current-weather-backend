from requests import get
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

import os

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def root():
    response = RedirectResponse(url="/current/weather", status_code=200)
    return response


@app.get("/current/weather")
def get_weather(lat: str, long: str):
    query = (f"{os.environ.get("CURRENT_WEATHER_ENDPOINT")}lat={lat}&lon={long}&units="
             f"{os.environ.get("CURRENT_WEATHER_UNITS")}&lang={os.environ.get("CURRENT_WEATHER_LANG")}"
             f"&appid={os.environ.get("CURRENT_WEATHER_KEY")}")

    response = get(query)

    if response.status_code == 200:
        return JSONResponse(response.json())

    return JSONResponse({"error": response.status_code})

