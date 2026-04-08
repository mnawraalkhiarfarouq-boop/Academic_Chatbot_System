import sqlite3

def chatbot_response(user_input):
    # الاتصال بقاعدة البيانات
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # البحث عن السؤال في قاعدة البيانات (تقنية المطابقة النصية)
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_input + '%',))
    row = cursor.fetchone()
    
    conn.close()
    
    if row:
        return row[0]
    else:
        return "عذراً، لم أجد إجابة دقيقة في لوائح الكلية حالياً. يرجى مراجعة مكتب الشؤون العلمية."

# تجربة المحادثة
if __name__ == "__main__":
    print("--- نظام المحادثة الأكاديمي الذكي قيد التشغيل ---")
    question = "متى تبدأ امتحانات الفصل الدراسي؟"
    print(f"الطالب يسأل: {question}")
    print(f"رد البوت: {chatbot_response(question)}")
