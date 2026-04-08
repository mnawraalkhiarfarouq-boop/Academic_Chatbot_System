from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_response(user_query):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    # البحث عن السؤال في قاعدة البيانات
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_query + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "عذراً، لم أجد إجابة دقيقة. يرجى مراجعة المسجل."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    bot_answer = get_db_response(user_message)
    return jsonify({'answer': bot_answer})

if __name__ == "__main__":
    app.run(debug=True)
