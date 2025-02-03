import ollama

def safe_chat(prompt: str) -> str:
    try:
        response = ollama.chat(
            model='llama3.1',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response['message']['content']
    except Exception as e:
        return f"เกิดข้อผิดพลาด: {str(e)}"
