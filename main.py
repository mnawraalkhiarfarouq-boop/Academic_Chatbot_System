from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get("message", "").lower()
    
    # 1. الاستعلام عن بداية الفصل الدراسي
    if "بداية" in msg or "متى يبدأ" in msg:
        sem = query_db("SELECT name, start_date FROM semesters LIMIT 1", one=True)
        response = f"يبدأ {sem[0]} بتاريخ {sem[1]}." if sem else "لم يتم تحديد موعد البداية بعد."

    # 2. الاستعلام عن جدول المحاضرات لقسم معين
    elif "جدول" in msg and ("نظم" in msg or "حاسوب" in msg):
        dept_name = "نظم المعلومات" if "نظم" in msg else "علوم الحاسوب"
        data = query_db("""
            SELECT l.day, c.name, l.start_time, s.name 
            FROM lectures l 
            JOIN courses c ON l.course_id = c.id 
            JOIN semesters s ON c.semester_id = s.id
            JOIN departments d ON c.dept_id = d.id
            WHERE d.name LIKE ? """, ('%' + dept_name + '%',))
        
        if data:
            details = [f"[{d[3]}] {d[0]}: {d[1]} (الساعة {d[2]})" for d in data]
            response = f"جدول محاضرات قسم {dept_name}: " + " | ".join(details)
        else:
            response = f"لا يوجد جدول متاح حالياً لقسم {dept_name}."

    # 3. الاستعلام عن النتائج أو اللوائح (البقاء على التفاصيل السابقة)
    elif "نتيجة" in msg:
        res = query_db("SELECT student_name, grade FROM results LIMIT 1", one=True)
        response = f"النتيجة المسجلة لـ {res[0]} هي {res[1]}" if res else "النتائج لم تصدر بعد."
    
    elif "لائحة" in msg:
        reg = query_db("SELECT content FROM regulations LIMIT 1", one=True)
        response = reg[0] if reg else "اللوائح متوفرة في قسم الشؤون العلمية."

    else:
        response = "مرحباً! يمكنني مساعدتك في معرفة جداول الأقسام، الفصول الدراسية، اللوائح، والنتائج."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
