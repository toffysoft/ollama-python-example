import ollama

# สร้างการสนทนาแบบง่าย
def simple_chat():
    response = ollama.chat(model='llama3.1', 
                          messages=[
                              {'role': 'user', 
                               'content': 'สวัสดี คุณทำอะไรได้บ้าง?'}
                          ])
    print(response['message']['content'])

# ทดสอบเรียกใช้งาน
if __name__ == '__main__':
    simple_chat()
