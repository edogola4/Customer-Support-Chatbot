from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_APIKEY'))

conversationarray = [{"role": "system", "content": "You are an assistant."}]
print("How can I help you? - Type 'stop' when you are done.")

while True:
    inputquestion = input("Question: ")
    
    if inputquestion.lower() == 'stop': break
    
    conversationarray.append({"role": "system", "content": inputquestion})
    
    response = client.chat.completions.create(
        model=os.getenv('TRAINED_MODEL_ID'),
        messages=conversationarray,
        temperature=0
    )
    
    assistant_response = response.choices[0].message.content
    
    conversationarray.append({"role": "assistant", "content": assistant_response})
    
    print(f"Assistant: {assistant_response}")