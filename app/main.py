from fastapi import FastAPI

app = FastAPI(title="PulseManager")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PulseManager",
        "mode": "manual-first"
    }
from app.core.reply_generator import ReplyGenerator
from app.core.inbox import InboxMessage, Platform

if __name__ == "__main__":
    # Quick test
    generator = ReplyGenerator()
    test_msg = InboxMessage(platform=Platform.instagram, author="Alice", content="Hello!")
    print("Draft reply:", generator.generate_reply(test_msg))
