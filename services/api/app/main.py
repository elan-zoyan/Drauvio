from fastapi import FastAPI

app = FastAPI(
    title="Drauvio Api",
    version="0.0.1"
)

@app.get("/")
def home():
    return{"message": "Welcome to Drauvio"}

@app.get("/health")
def health_check():
    return {"status":"ok"}




