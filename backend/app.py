from fastapi import FastAPI

app = FastAPI(
    title="Enterprise RAG Knowledge Assistant",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Knowledge Assistant Running"
    }
