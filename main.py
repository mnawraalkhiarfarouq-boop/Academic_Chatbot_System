from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# وظيفة للبحث في اللوائح والامتحانات
def search_academic_info(query):
    # محاكاة للرد الذكي بناءً على أهداف مشروعك
    knowledge = {
        "لوائح": "لائحة الكلية تنص على ضرورة حضور 75% من المحاضرات لدخول الامتحان.",
        "امتحان": "جدول امتحانات الفصل الدراسي الأول سيبدأ في الأسبوع الثاني من يناير.",
        "جدول": "يمكنك العثور على جدولك الدراسي في لوحة الإعلانات الإلكترونية."
    }
    for key in knowledge:
        if key in query: return knowledge[key]
    return "عذراً، تواصل مع الشؤون الأكاديمية لمزيد من التفاصيل حول هذا الموضوع."

@app.route('/ask', methods=['POST'])
def ask():
    user_query = request.json.get("message")
    response = search_academic_info(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
