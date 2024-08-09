import requests

def analyze_code(code):
    api_key = "AIzaSyCzl1u-d6utmVWalopg6fK23-VO2ZlRN1Q"
    payload = {
        "code": code,
        "key": api_key
    }
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to analyze code"}
