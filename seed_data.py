import sqlite3

def seed():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # إضافة الأقسام
    cursor.executemany("INSERT OR IGNORE INTO departments (id, name) VALUES (?, ?)", [(1, 'نظم المعلومات'), (2, 'علوم الحاسوب')])

    # إضافة الفصول الدراسية وتاريخ البداية
    cursor.executemany("INSERT OR IGNORE INTO semesters (id, name, start_date) VALUES (?, ?, ?)", 
                       [(1, 'الفصل الدراسي الأول', '2026-01-15'), (2, 'الفصل الدراسي الثالث', '2026-01-20')])

    # إضافة مواد (لكل قسم وفصل)
    courses = [
        (1, 'قواعد البيانات 1', 1, 1), # مادة لقسم نظم المعلومات - فصل 1
        (2, 'تحليل نظم المعلومات', 1, 2), # مادة لقسم نظم المعلومات - فصل 3
        (3, 'خوارزميات', 2, 2)            # مادة لقسم علوم الحاسوب - فصل 3
    ]
    cursor.executemany("INSERT OR IGNORE INTO courses (id, name, dept_id, semester_id) VALUES (?, ?, ?, ?)", courses)

    # إضافة جدول المحاضرات
    lectures = [
        (1, 'الأحد', '08:00', 'قاعة 1'),
        (2, 'الثلاثاء', '10:00', 'معمل الحاسوب'),
        (3, 'الإثنين', '12:00', 'قاعة الرازي')
    ]
    cursor.executemany("INSERT OR IGNORE INTO lectures (course_id, day, start_time, room) VALUES (?, ?, ?, ?)", lectures)

    # إضافة اللوائح والنتائج
    cursor.execute("INSERT OR IGNORE INTO regulations (title, content) VALUES ('الحضور', 'يمنع الطالب من الامتحان إذا تجاوز غيابه 25%')")
    cursor.execute("INSERT OR IGNORE INTO results (student_name, course_id, grade) VALUES ('منيرة الخير', 1, 'A')")

    conn.commit()
    conn.close()
    print("✅ تم ملء البيانات: الأقسام، جداول المحاضرات، اللوائح، والنتائج!")

if __name__ == "__main__": seed()
