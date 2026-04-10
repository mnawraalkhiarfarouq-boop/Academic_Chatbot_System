import sqlite3

def init_db():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # 1. الأقسام والفصول الدراسية
    cursor.execute('CREATE TABLE IF NOT EXISTS departments (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS semesters (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, start_date TEXT)')

    # 2. المواد (مرتبطة بقسم وفصل معين)
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        dept_id INTEGER, 
        semester_id INTEGER,
        FOREIGN KEY(dept_id) REFERENCES departments(id),
        FOREIGN KEY(semester_id) REFERENCES semesters(id)
    )''')

    # 3. جدول المحاضرات (الزمان والمكان)
    cursor.execute('''CREATE TABLE IF NOT EXISTS lectures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER,
        day TEXT,
        start_time TEXT,
        room TEXT,
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )''')

    # 4. اللوائح، الامتحانات، والنتائج
    cursor.execute('CREATE TABLE IF NOT EXISTS regulations (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS exams (id INTEGER PRIMARY KEY AUTOINCREMENT, course_id INTEGER, date TEXT, hall TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY AUTOINCREMENT, student_name TEXT, course_id INTEGER, grade TEXT)')

    conn.commit()
    conn.close()
    print("✅ تم تحديث قاعدة البيانات لتشمل الأقسام والجداول واللوائح والنتائج!")

if __name__ == "__main__":
    init_db()
