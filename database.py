import sqlite3

def init_db():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # جدول الصلاحيات والمستخدمين
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT, -- 'student', 'doctor', 'admin'
        department TEXT
    )''')

    # جدول الكليات (كما في شكل 29.4)
    cursor.execute('''CREATE TABLE IF NOT EXISTS colleges (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        details TEXT
    )''')

    # جدول المواد (كما في شكل 31.4)
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        course_code TEXT
    )''')

    # جدول الاستشارات والمشاكل (كما في شكل 22.4 و 27.4)
    cursor.execute('''CREATE TABLE IF NOT EXISTS inquiries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        category TEXT, -- 'academic', 'health', 'social'
        question TEXT,
        answer TEXT,
        status TEXT DEFAULT 'pending',
        FOREIGN KEY(student_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
