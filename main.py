import sqlite3


conn = sqlite3.connect("university.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        major TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        instructor TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")

conn.commit()


while True:
    print("\n1. Add a new student")
    print("2. Add a new course")
    print("3. Show students")
    print("4. Show courses")
    print("5. Change student")
    print("6. Change course")
    print("7. Register a student for a course")
    print("8. Students on the course")
    print("0. Exit")

    choice = input(">>> ")

    ...
