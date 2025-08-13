import requests
import json

# API的URL
url = 'http://localhost:11434/api/chat'
input_text = "你好"

# 要发送的数据
data = {
    "model": "deepseek-r1:7b",
    "messages": [
        {"role": "system", "content": "你是一个数学家，你可以计算任何算式。"},
        {"role": "user", "content": " "}
    ],
    "stream": False
}

# 找到role为user的message
for message in data["messages"]:
    if message["role"] == "user":
        # 将输入文本添加到content的开头
        message["content"] = input_text

# 将字典转换为JSON格式的字符串
json_data = json.dumps(data)

try:
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
    response.raise_for_status()  # 检查HTTP错误[3]()

    # 解析JSON并提取回复内容
    result = response.json()
    if 'message' in result and 'content' in result['message']:
        print("大模型回复：", result['message']['content'])
    else:
        print("未找到有效回复，完整响应：", json.dumps(result, indent=2, ensure_ascii=False))

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP错误：{http_err}")
except json.JSONDecodeError:
    print("响应内容非JSON格式：", response.text)
except Exception as e:
    print(f"其他错误：{str(e)}")
