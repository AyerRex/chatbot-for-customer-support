from typing import Dict, Any, List, Tuple, Optional
from sqlalchemy.orm import Session

from models import Order, User


def get_quick_replies(intent: str) -> List[str]:
    """
    Suggestions to show in the UI depending on last intent.
    (keep for button)
    """
    if intent == "greet":
        return ["Ask about shirts", "Check order status", "Return / exchange policy"]
    if intent == "product_info":
        return ["What sizes are available?", "Do you have black shirts?", "What is the material?"]
    if intent == "order_status":
        return ["My order status", "I want to update my address"]
    if intent == "returns":
        return ["How do I return a shirt?", "What is your refund policy?"]
    return ["Ask about shirts", "Check order status", "Return / exchange policy"]


def handle_intent(
        intent: str,
        entities: Dict[str, Any],
        db: Session,
) -> Tuple[Optional[str], Dict[str, Any]]:
    """
    Modified: Logic removed to let Rasa Core & Action Server handle the conversation.
    Returns (None, payload) so main.py knows to use Rasa's response.
    """
    payload: Dict[str, Any] = {}

    # This section retains the payload processing, the fronted may still need to use user_identifier
    user_identifier: Optional[str] = entities.get("user_identifier")

    # ---------------------------------------------------------
    # All comment out
    # No need hard code any more, let Rasa decied
    # ---------------------------------------------------------

    # if intent == "greet":
    #     text = (
    #         "Hi! 👋 I'm your shirt support assistant. I can help with product info, "
    #         "order status (for signed-in customers), and returns. What would you like to do?"
    #     )
    #     return text, payload

    # if intent == "abusive":
    #     text = (
    #         "I'm here to help. Let's keep the conversation respectful. "
    #         "How can I assist you with your order or shirts?"
    #     )
    #     return text, payload

    # if intent == "goodbye":
    #     text = "Thanks for chatting with us! If you need anything else, just open the chat again. 😊"
    #     return text, payload

    # # --- Business intents below ---

    # if intent == "product_info":
    #     text = (
    #         "We sell men's and women's shirts in sizes XS–XXL. "
    #         "Most shirts are 100% cotton or cotton blends. "
    #         "What would you like to know: size, colour, or material?"
    #     )
    #     return text, payload

    # if intent == "returns":
    #     text = (
    #         "Our return policy: you can return or exchange shirts within 30 days "
    #         "of delivery, as long as tags are intact and the shirt is unworn. "
    #         "Would you like steps for starting a return?"
    #     )
    #     return text, payload

    # # 🔐 Order status: login required
    # if intent == "order_status":
    #     # ... (Originally a very long DB query logic omitted) ...
    #     # Originally, this would intercept ORD-67890 and return "not found"
    #     pass 

    # ---------------------------------------------------------
    # Return None
    # Tell main.py: I have no processing logic here, please use the answer returned by Rasa.
    # ---------------------------------------------------------
    return None, payload