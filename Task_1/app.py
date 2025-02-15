from flask import Flask, render_template, request, jsonify
from chatbot import *

app = Flask(__name__)
chatbot = ChatBot()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = chatbot.generate_response(user_input)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)