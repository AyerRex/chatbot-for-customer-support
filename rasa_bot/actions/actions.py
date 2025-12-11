from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionCheckOrderStatus(Action):

    def name(self) -> Text:
        return "action_check_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # 1. Get the order number from the slot
        order_id = tracker.get_slot("order_number")

        # 2. Mock Database Lookup (Simulating backend logic)
        # In a real scenario, you would call your FastAPI/DB here.
        if not order_id or " " in order_id or len(order_id) > 20:
            return [SlotSet("order_number", None)]

        # Convert to specific format for matching mock data if needed
        order_id_clean = order_id.upper().strip()

        if order_id_clean == "ORD-12345":
            status = "Shipped - Estimated delivery: Tomorrow"
        elif order_id_clean == "ORD-67890":
            status = "Processing - Waiting for payment"
        elif order_id_clean == "ORD-99999":
            status = "Delivered - Left at front porch"
        else:
            status = "Not Found - Please check your order ID"

        # 3. Respond to the user in English
        response_text = f"The status for order {order_id} is: {status}"
        dispatcher.utter_message(text=response_text)

        # 4. Clear the slot so the user can check another order later
        return [SlotSet("order_number", None)]