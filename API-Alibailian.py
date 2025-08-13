import os
from openai import OpenAI

os.environ[
    "OPENAI_API_KEY"] = "到阿里百炼配置阿里百炼 API 密钥"  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
    extra_body={"enable_thinking": False},
)
print(completion.model_dump_json())
