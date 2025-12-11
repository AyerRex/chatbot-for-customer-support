# backend/rasa_client.py
import os
import requests

RASA_URL = os.getenv("RASA_URL", "http://rasa:5005/model/parse")
# 🆕 New URL for full conversation flow (Core + Action Server)
RASA_WEBHOOK_URL = "http://rasa:5005/webhooks/rest/webhook"

def parse_message(message: str):
    """
    Uses Rasa NLU to get intent and entities only.
    Does NOT trigger the Action Server or Stories.
    """
    payload = {"text": message}
    try:
        r = requests.post(RASA_URL, json=payload)
        r.raise_for_status()
        data = r.json()
        intent = data.get("intent", {}).get("name")
        entities = {e["entity"]: e["value"] for e in data.get("entities", [])}
        return intent, entities
    except Exception as e:
        print(f"Rasa NLU Error: {e}")
        return None, {}

def get_rasa_response(message: str, sender_id: str):
    """
    🆕 Sends the message to Rasa Core via Webhook.
    This triggers the dialogue flow, stories, rules, and CUSTOM ACTIONS.
    """
    payload = {
        "sender": sender_id,  # Conversation ID (so Rasa remembers context)
        "message": message
    }
    try:
        print(f"DEBUG: Sending to Rasa at {RASA_WEBHOOK_URL} with payload: {payload}")  # <--- 新增這行
        r = requests.post(RASA_WEBHOOK_URL, json=payload, timeout=10)  # <--- 加上 timeout=10 防止無限等待
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"🔥 CRITICAL RASA ERROR: {e}")  # <--- 讓錯誤更顯眼
        import traceback
        traceback.print_exc()  # <--- 印出完整錯誤堆疊
        return []