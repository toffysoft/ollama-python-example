import ollama

from typing import List, Dict

class ChatAssistant:
    def __init__(self, model_name: str = 'llama3.1'):
        self.model = model_name
        self.conversation_history: List[Dict[str, str]] = []
    
    def chat(self, message: str) -> str:
        # เพิ่มข้อความใหม่เข้าไปในประวัติการสนทนา
        self.conversation_history.append({
            'role': 'user',
            'content': message
        })
        
        # ส่งประวัติการสนทนาทั้งหมดไปให้ LLM
        response = ollama.chat(
            model=self.model,
            messages=self.conversation_history
        )
        
        # เก็บการตอบกลับลงในประวัติ
        self.conversation_history.append({
            'role': 'assistant',
            'content': response['message']['content']
        })
        
        return response['message']['content']
    
    def clear_history(self):
        self.conversation_history = []
