import configparser
from openai import OpenAI

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

client = OpenAI(
    api_key=config['llm']['api_key'],
    base_url=config['llm']['base_url']
)

user_input = input("你: ")

response = client.chat.completions.create(
    model=config['llm']['model'],
    messages=[{"role": "user", "content": user_input}]
)

print("AI:", response.choices[0].message.content)
