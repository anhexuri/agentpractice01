import configparser
from openai import OpenAI

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

client = OpenAI(
    api_key=config['llm']['api_key'],
    base_url=config['llm']['base_url']
)

while True:
    user_input = input("你: ")

    print("AI: ", end="", flush=True)
    stream = client.chat.completions.create(
        model=config['llm']['model'],
        messages=[{"role": "user", "content": user_input}],
        stream=True
    )

    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()
