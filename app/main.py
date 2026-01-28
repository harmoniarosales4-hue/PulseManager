from fastapi import FastAPI
from app.core.reply_generator import ReplyGenerator
from app.core.inbox import InboxMessage, Platform
from app.core.inbox_store import InboxStore
from app.core.approval import ApprovalManager

# -----------------------------
# FastAPI app setup
# -----------------------------
app = FastAPI(title="PulseManager")

# In-memory inbox
inbox = InboxStore()
approval_manager = ApprovalManager(inbox)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "PulseManager",
        "mode": "manual-first"
    }

# -----------------------------
# Quick test (runs only when executing main.py directly)
# -----------------------------
if __name__ == "__main__":
    # ----- Test ReplyGenerator -----
    generator = ReplyGenerator()
    test_msg1 = InboxMessage(
        platform=Platform.instagram,
        author="Alice",
        content="Hello!"
    )
    print("Draft reply (ReplyGenerator):", generator.generate_reply(test_msg1))

    # ----- Test ApprovalManager -----
    test_msg2 = InboxMessage(
        platform=Platform.reddit,
        author="Bob",
        content="Nice post!"
    )
    draft = approval_manager.create_draft(test_msg2)
    print("Draft created (ApprovalManager):", draft)

    pending = approval_manager.list_pending()
    print("Pending messages:", pending)

    approved = approval_manager.approve_message(test_msg2.id)
    print("Approved message:", approved)
