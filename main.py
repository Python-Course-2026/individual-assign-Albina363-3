from fastapi import FastAPI
from router import router

app = FastAPI(title="Password Generator API", version="1.0.0")
app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Добро пожаловать в Password Generator API",
        "docs": "/docs",
    }
