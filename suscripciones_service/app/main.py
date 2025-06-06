from fastapi import FastAPI

app = FastAPI(title="Microservicio de Suscripciones")

@app.get("/")
async def root():
    return {"message": "¡Suscripciones funcionando!"}
