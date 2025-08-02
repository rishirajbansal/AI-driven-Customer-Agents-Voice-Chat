
# vapi_integration.py
import requests

VAPI_API_KEY = "VAPI_API_KEY_CONFIDENTIAL"

def initiate_voice_call(to_number, message_text):
    url = "https://api.vapi.ai/call"
    payload = {
        "to": to_number,
        "message": message_text,
    }
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()
