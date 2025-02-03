import ollama

def stream_chat(prompt: str):
    stream = ollama.chat(
        model='llama3.1',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True
    )
    
    # พิมพ์ข้อความทีละส่วนตามที่ได้รับ
    for chunk in stream:
        if chunk['message']['content']:
            print(chunk['message']['content'], end='', flush=True)
