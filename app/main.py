from fastapi import FastAPI

app = FastAPI(title="PulseManager")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PulseManager",
        "mode": "manual-first"
    }
