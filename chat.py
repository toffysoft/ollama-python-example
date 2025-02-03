from assistant import ChatAssistant

assistant = ChatAssistant()

questions = [
    "Python คืออะไร?",
    "ยกตัวอย่างการใช้งาน list comprehension",
    "แล้ว dictionary comprehension ล่ะ?"
]

for question in questions:
    print(f"\nคำถาม: {question}")
    print(f"คำตอบ: {assistant.chat(question)}")
