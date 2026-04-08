import sqlite3

# إنشاء ملف قاعدة البيانات
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# إنشاء جدول الطلاب والنتائج والجداول
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, level INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS results (student_id INTEGER, subject TEXT, grade TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS schedules (subject TEXT, day TEXT, time TEXT)')

conn.commit()
conn.close()
print("تم تجهيز قاعدة البيانات بنجاح!")
