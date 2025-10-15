from fastapi import FastAPI

from src.api.routes import router as api_router

app = FastAPI(title="FastAPI + SvelteKit Starter")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI + SvelteKit project!"}


app.include_router(api_router, prefix="/api")
