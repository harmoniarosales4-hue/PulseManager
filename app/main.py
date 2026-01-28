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
from app.core.approval import ApprovalManager

approval_manager = ApprovalManager(inbox)

# Quick manual test
if __name__ == "__main__":
    test_msg = InboxMessage(platform=Platform.reddit, author="Bob", content="Nice post!")
    draft = approval_manager.create_draft(test_msg)
    print("Draft created:", draft)

    pending = approval_manager.list_pending()
    print("Pending messages:", pending)

    approved = approval_manager.approve_message(test_msg.id)
    print("Approved message:", approved)
