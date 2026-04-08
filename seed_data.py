import sqlite3

def add_data():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # إضافة أسئلة وأجوبة تجريبية (اللوائح)
    faq_data = [
        ('متى تبدأ امتحانات الفصل الدراسي؟', 'تبدأ الامتحانات عادة في الأسبوع الثالث من شهر يونيو.'),
        ('كيف يمكنني استخراج كشف درجات؟', 'يمكنك مراجعة مكتب المسجل بالطابق الأول لإكمال الإجراءات.'),
        ('أين يقع معمل الحاسوب رقم 1؟', 'يقع في الجناح الغربي من الكلية.')
    ]
    cursor.executemany("INSERT INTO faq (question, answer) VALUES (?, ?)", faq_data)

    # إضافة بيانات طالب تجريبي (أنتِ مثلاً!)
    cursor.execute("INSERT INTO students (name, level, department) VALUES ('منوره الخير', 4, 'علوم الحاسوب')")

    conn.commit()
    conn.close()
    print("تمت إضافة البيانات التجريبية بنجاح!")

if __name__ == "__main__":
    add_data()
