from datetime import datetime
from typing import Optional
from app.core.inbox import InboxMessage, MessageStatus
from app.core.inbox_store import InboxStore
from app.core.reply_generator import ReplyGenerator


class ApprovalManager:
    """
    Handles manual approval workflow for draft replies.
    """

    def __init__(self, inbox: InboxStore):
        self.inbox = inbox
        self.generator = ReplyGenerator()

    def create_draft(self, message: InboxMessage) -> str:
        """
        Generate a draft reply for a message and store it.
        """
        draft = self.generator.generate_reply(message)
        message.reply_draft = draft
        message.status = MessageStatus.pending
        self.inbox.add_message(message)
        return draft

    def approve_message(self, message_id: str) -> Optional[InboxMessage]:
        """
        Approve a message, marking it as replied.
        """
        for msg in self.inbox.messages:
            if msg.id == message_id:
                msg.status = MessageStatus.replied
                msg.replied_at = datetime.utcnow()
                return msg
        return None

    def ignore_message(self, message_id: str) -> Optional[InboxMessage]:
        """
        Ignore a message, marking it as ignored.
        """
        for msg in self.inbox.messages:
            if msg.id == message_id:
                msg.status = MessageStatus.ignored
                return msg
        return None

    def list_pending(self):
        """
        Return all pending messages.
        """
        return [m for m in self.inbox.messages if m.status == MessageStatus.pending]
