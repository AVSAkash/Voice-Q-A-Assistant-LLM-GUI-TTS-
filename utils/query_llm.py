import httpx
from config import OPENROUTER_API_KEY, MODEL

def stream_llm_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://github.com/your-github",  # optional
        "X-Title": "Voice QnA App"
    }

    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    with httpx.stream("POST", "https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data) as r:
        for line in r.iter_lines():
            if line and line.startswith("data: "):
                chunk = line.replace("data: ", "")
                if chunk == "[DONE]":
                    break
                try:
                    content = httpx.Response(200, content=chunk).json()
                    yield content["choices"][0]["delta"].get("content", "")
                except Exception:
                    continue
