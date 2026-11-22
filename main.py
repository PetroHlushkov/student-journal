import sqlite3


conn = sqlite3.connect("university.db")
cursor = conn.cursor()

conn.execute("PRAGMA foreign_keys = ON")

# Example `students` table:
# ====================================
# id | name | age | major            |
# 1  | John | 21  | Computer Science |
# 2  | Jane | 19  | Physics          |
# ====================================
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
""")

# Example `courses` table:
# ======================================
# course_id | course_name | instructor |
# 1         | Mathematics | Robert     |
# 2         | Physics     | Michael    |
# ======================================
cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        instructor TEXT
    )
""")

# Example `student_courses` table:
# ========================
# student_id | course_id |
# 1          | 1         |
# 1          | 2         |
# 2          | 2         |
# ======================== 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY (student_id, course_id),
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
    print("5. Update student information")
    print("6. Update student information")
    print("7. Register a student for a course")
    print("8. Students enrolled in a course")
    print("0. Exit")

    choice = input(">>> ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        major = input("Enter student major: ")

        cursor.execute("""
            INSERT INTO students (name, age, major)
            VALUES (?, ?, ?)
        """, (name, age, major))

    elif choice == "2":
        course_name = input("Enter course name: ")
        instructor = input("Enter instructor name: ")

        cursor.execute("""
            INSERT INTO courses (course_name, instructor)
            VALUES (?, ?)
        """, (course_name, instructor))

    elif choice == "3":
        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        if not students:
            print("\nNo students found.")
        else:
            print("\n---- Students ----")

            for student in students:
                print("░ ID:", student[0])
                print("▓ Name:", student[1])
                print("░ Age:", student[2])
                print("▓ Major:", student[3])

            print("------------------")

    elif choice == "4":
        cursor.execute("SELECT * FROM courses")
        
        students = cursor.fetchall()

        if not students:
            print("\nNo courses found.")
        else:
            print("\n---- Courses ----")

            for student in students:
                print("░ ID:", student[0])
                print("▓ Name:", student[1])
                print("▓ Instructor:", student[2])

            print("-----------------")

    elif choice == "5":
        pass

    elif choice == "6":
        pass

    elif choice == "7":
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))

        cursor.execute("""
            INSERT INTO student_courses (student_id, course_id)
            VALUES (?, ?)
        """, (student_id, course_id))

    elif choice == "8":
        pass

    elif choice == "0":
        break

conn.close()
