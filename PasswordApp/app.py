# app.py
from flask import Flask, render_template, jsonify, request
from passwordGenerator import generatePassword

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data.get('lengthEntry', 12))
    nums = data.get('nums', False)
    uppers = data.get('uppers', False)
    symbols = data.get('symbols', False)
    password = generatePassword(length, nums, uppers, symbols)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True)
