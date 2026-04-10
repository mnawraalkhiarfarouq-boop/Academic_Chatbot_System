import sqlite3

def seed_project():
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()
    
    # إضافة مستخدمين تجريبيين (طالب، دكتور، مدير)
    users = [
        ('student_user', '123', 'student', 'Information Systems'),
        ('doctor_kawthar', '456', 'doctor', 'Computer Science'),
        ('admin_user', '789', 'admin', 'Administration')
    ]
    cursor.executemany("INSERT OR IGNORE INTO users (username, password, role, department) VALUES (?, ?, ?, ?)", users)
    
    # إضافة بيانات الكلية (كما في واجهة الإدارة 29.4)
    colleges = [('كلية الحاسوب وتقانة المعلومات', 'أم درمان - المدينة الجامعية', 'تأسست عام 2007')]
    cursor.executemany("INSERT OR IGNORE INTO colleges (name, location, details) VALUES (?, ?, ?)", colleges)

    conn.commit()
    conn.close()
    print("✅ تم تحديث بيانات النظام بنجاح!")

if __name__ == "__main__":
    seed_project()
