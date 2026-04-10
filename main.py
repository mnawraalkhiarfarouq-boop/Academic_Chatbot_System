from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# محرك الرد الآلي (لحل مشكلة بطء الاستجابة)
def academic_ai_logic(text):
    knowledge_base = {
        "التسجيل": "يبدأ التسجيل لكلية الحاسوب في 15 مايو عبر البوابة الإلكترونية.",
        "الامتحانات": "جداول الامتحانات النهائية ستصدر في الأسبوع القادم في قسم الإعلانات.",
        "تجميد": "لتقديم طلب تجميد، يجب مراجعة مكتب الشؤون الأكاديمية بالكلية."
    }
    for key in knowledge_base:
        if key in text: return knowledge_base[key]
    return None

@app.route('/ask', methods=['POST'])
def handle_inquiry():
    data = request.json
    user_id = data.get('user_id')
    question = data.get('question')
    
    # محاولة الرد آلياً أولاً
    auto_reply = academic_ai_logic(question)
    
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    if auto_reply:
        cursor.execute("INSERT INTO inquiries (student_id, question, answer, status) VALUES (?, ?, ?, ?)",
                       (user_id, question, auto_reply, 'completed'))
        response = {"reply": auto_reply, "type": "automated"}
    else:
        # إذا لم يجد رداً، يحولها كـ "مشكلة" للدكتور (كما في شكل 27.4)
        cursor.execute("INSERT INTO inquiries (student_id, question, status) VALUES (?, ?, ?)",
                       (user_id, question, 'pending'))
        response = {"reply": "تم تحويل سؤالك للمشرف الأكاديمي، سيصلك الرد قريباً.", "type": "manual"}
    
    conn.commit()
    conn.close()
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
