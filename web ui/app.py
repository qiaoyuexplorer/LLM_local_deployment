from flask import Flask, request, jsonify, render_template
from http import HTTPStatus
import dashscope

app = Flask(__name__)

# 配置阿里百炼 API 密钥
dashscope.api_key = "到阿里百炼配置阿里百炼 API 密钥"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])

    try:
        responses = dashscope.Generation.call(
            model="qwen-max",
            messages=messages,
            stream=True,
            result_format='message',
            top_p=0.8,
            temperature=0.7,
            enable_search=False,
            # enable_thinking=False,
            enable_thinking=True,
            incremental_output=True,  # 添加这个参数
            thinking_budget=4000
        )

        # 收集所有响应片段
        full_response = ""
        for response in responses:
            if response.status_code == HTTPStatus.OK:
                if 'content' in response.output.choices[0]['message']:
                    full_response += response.output.choices[0]['message']['content']
            else:
                return jsonify({
                    'error': f'Request failed with status code {response.status_code}',
                    'message': response.message
                }), 400

        return jsonify({
            'response': full_response
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)