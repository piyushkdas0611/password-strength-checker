from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    # Add your password strength criteria checks here
    length_check = len(password) >= 8
    complexity_check = re.search(r"[A-Za-z]+", password) and re.search(r"\d+", password)
    uniqueness_check = len(set(password)) == len(password)

    return length_check and complexity_check and uniqueness_check

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password_strength', methods=['POST'])
def check_password():
    password = request.form['password']
    is_strong = check_password_strength(password)
    return jsonify({'is_strong': is_strong})

if __name__ == '__main__':
    app.run(debug=True)
