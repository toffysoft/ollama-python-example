import ollama

def advanced_chat(prompt: str):
    response = ollama.chat(
        model='llama3.1',
        messages=[{'role': 'user', 'content': prompt}],
        options={
            'temperature': 0.7,  # ควบคุมความสร้างสรรค์ (0.0 - 1.0)
            'top_p': 0.9,       # ควบคุมความหลากหลายของคำตอบ
            'top_k': 40,        # จำนวนโทเค็นที่พิจารณา
            'num_predict': 4069  # ความยาวสูงสุดของคำตอบ
        }
    )
    return response['message']['content']

# ทดสอบเรียกใช้งาน
if __name__ == '__main__':
    prompt = "เล่าเรื่องตลกให้ฟังหน่อยสิ"
    print(advanced_chat(prompt))