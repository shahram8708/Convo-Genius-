import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import markdown

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/user-details', methods=['GET'])
def user_details():
    return render_template('user-details.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.form['user_input']
    if user_input.lower() != 'exit':
        response = chat.send_message(user_input)
        bot_response = response.text 
        bot_response_html = markdown.markdown(bot_response)
    else:
        bot_response_html = markdown.markdown("Chat ended. Please refresh the page to start a new chat.")
    
    return jsonify(user_input=user_input, bot_response=bot_response_html)

if __name__ == '__main__':
    app.run(debug=True)