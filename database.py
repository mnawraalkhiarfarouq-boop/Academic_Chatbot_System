import sqlite3

def init_db():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # 1. جدول اللوائح الجامعية (قواعد عامة)
    cursor.execute('''CREATE TABLE IF NOT EXISTS regulations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )''')

    # 2. جدول المواد الدراسية (كما في شكل 31.4)
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        course_code TEXT
    )''')

    # 3. جدول جداول الامتحانات
    cursor.execute('''CREATE TABLE IF NOT EXISTS exam_schedules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER,
        exam_date TEXT,
        exam_time TEXT,
        hall_number TEXT,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )''')

    conn.commit()
    conn.close()
    print("✅ تم تحديث جداول اللوائح والامتحانات بنجاح")

if __name__ == "__main__":
    init_db()
