from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "OK", "message": "Backend is running 🚀"}

@app.get("/health")
def health():
    return {"ok": True}
