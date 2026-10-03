from fastapi import FastAPI

app = FastAPI(
    title="API de gerenciamento do Facebook",
    version="0.1.0",
    description="Camada segura de integração com a Meta Graph API.",
)


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
