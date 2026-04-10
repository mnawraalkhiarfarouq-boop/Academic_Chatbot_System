import sqlite3

def seed_academic_data():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # 1. إدخال اللوائح الأكاديمية (Academic Regulations)
    regulations = [
        ('نسبة الحضور', 'يجب على الطالب حضور 75% من المحاضرات كحد أدنى لدخول الامتحان النهائي.'),
        ('تجميد الدراسي', 'يسمح للطالب بتجميد العام الدراسي لمرة واحدة فقط خلال المسيرة الجامعية.'),
        ('الإنذار الأكاديمي', 'يُوضع الطالب تحت الإنذار إذا قل المعدل التراكمي عن 2.00.')
    ]
    cursor.executemany("INSERT OR IGNORE INTO regulations (title, content) VALUES (?, ?)", regulations)

    # 2. إدخال الأقسام (كما في شكل 30.4)
    departments = [
        ('نظم المعلومات', 'كلية الحاسوب', 'يهتم بدراسة تكنولوجيا المعلومات وإدارة البيانات'),
        ('علوم الحاسوب', 'كلية الحاسوب', 'يركز على البرمجة، الخوارزميات، والذكاء الاصطناعي')
    ]
    cursor.executemany("INSERT OR IGNORE INTO departments (dept_name, college_name, description) VALUES (?, ?, ?)", departments)

    # 3. إدخال المواد الدراسية (كما في شكل 31.4)
    courses = [
        ('قواعد البيانات', 'IS202', 1),
        ('هندسة البرمجيات', 'CS301', 2),
        ('الذكاء الاصطناعي', 'AI404', 2)
    ]
    cursor.executemany("INSERT OR IGNORE INTO courses (course_name, course_code, dept_id) VALUES (?, ?, ?)", courses)

    # 4. إدخال جداول الامتحانات
    exams = [
        (1, '2026-05-10', 'القاعة الكبرى'),
        (2, '2026-05-12', 'معمل الحاسوب 1'),
        (3, '2026-05-15', 'قاعة الرازي')
    ]
    cursor.executemany("INSERT OR IGNORE INTO exams (course_id, exam_date, exam_hall) VALUES (?, ?, ?)", exams)

    conn.commit()
    conn.close()
    print("✅ تم بنجاح تغذية النظام بكافة البيانات الأكاديمية (لوائح، مواد، جداول)!")

if __name__ == "__main__":
    seed_academic_data()
