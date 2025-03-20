import sys
import threading

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import door
import subprocess  # 用来执行本地程序

# 假设你的 Door 类存放在 your_door_module.py 文件中

app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


def run_createdoor(total_width, total_height, small_door_width, small_door_height, flag, bloster_type):
    result = subprocess.run(
        [sys.executable, 'createdoor.py', str(total_width), str(total_height), str(small_door_width),
         str(small_door_height), str(flag), str(bloster_type)], capture_output=True, text=True)
    output = result.stdout
    print("Output from createdoor.py:", output)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

@app.route('/create_door', methods=['POST'])
def create_door():
    try:
        # 获取前端传递的门的宽度和高度
        data = request.json
        total_width = data['total_width']
        total_height = data['total_height']
        small_door_width = data['small_door_width']
        small_door_height = data['small_door_height']
        flag = data['flag']
        bloster_type = data['bloster_type']
        print(total_width, total_height, small_door_width, small_door_height,flag,bloster_type)

        thread = threading.Thread(target=run_createdoor, args=(total_width, total_height, small_door_width, small_door_height, flag, bloster_type))
        thread.start()


        print('a')
        # 创建 Door 类实例
        # door = Door(total_width, total_height, small_door_width, small_door_height)

        # 你可以在这里调用 Door 类的方法来生成图形
        # door.create_hinge1(...) 等

        return jsonify({'status': 'success', 'message': f'Door created successfully.'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
