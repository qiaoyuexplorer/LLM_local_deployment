from openai import OpenAI

base_url = "https://api.ppinfra.com/v3/openai"
api_key = "此处APIKEY需要到https://ppio.com/console进行获取"

model = "qwen/qwen3-4b-fp8"

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

stream = True  # or False
max_tokens = 1000

response_format = {"type": "text"}

chat_completion_res = client.chat.completions.create(
    model=model,
    messages=[

        {
            "role": "user",
            "content": "Hi there!",
        }
    ],
    stream=stream,
    extra_body={}
)

if stream:
    for chunk in chat_completion_res:
        print(chunk.choices[0].delta.content or "", end="")
else:
    print(chat_completion_res.choices[0].message.content)

