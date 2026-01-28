from app.core.persona_loader import PersonaLoader
from app.core.inbox import InboxMessage

class ReplyGenerator:
    """
    Generates draft replies based on persona rules.
    """

    def __init__(self):
        self.persona = PersonaLoader().get_persona()

    def generate_reply(self, message: InboxMessage) -> str:
        """
        Generate a draft reply for a given InboxMessage.
        Currently returns a placeholder. 
        Later we can integrate AI/ML logic or OpenAI API.
        """
        # Simple placeholder logic
        draft = (
            f"Hi {message.author}, thank you for your message! "
            "I appreciate your comment. [Persona applied]"
        )
        return draft
