
from faker import Faker
import random
import sqlite3


fake = Faker()

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

cursor.execute('''DROP TABLE IF EXISTS Students''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                    student_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    group_id INTEGER,
                    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
                )''')

cursor.execute('''DROP TABLE IF EXISTS Groups''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Groups (
                    group_id INTEGER PRIMARY KEY,
                    group_name TEXT
                )''')

cursor.execute('''DROP TABLE IF EXISTS Subjects''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                    subject_id INTEGER PRIMARY KEY,
                    subject_name TEXT,
                    lecturer_id INTEGER,
                    FOREIGN KEY (lecturer_id) REFERENCES Lecturers(lecturer_id)
                )''')

cursor.execute('''DROP TABLE IF EXISTS Lecturers''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Lecturers (
                    lecturer_id INTEGER PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT
                )''')

cursor.execute('''DROP TABLE IF EXISTS Grades''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                    grade_id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    subject_id INTEGER,
                    grade DECIMAL(3,2),
                    grade_date DATE,
                    FOREIGN KEY (student_id) REFERENCES Students(student_id),
                    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
                )''')

# Dodanie danych do tabeli z grupami
groups_data = [(1, 'Group A'), (2, 'Group B'), (3, 'Group C')]
cursor.executemany(
    "INSERT INTO Groups (group_id, group_name) VALUES (?, ?)", groups_data)

lecturers_data = [(1, fake.first_name(), fake.last_name()),
                  (2, fake.first_name(), fake.last_name()),
                  (3, fake.first_name(), fake.last_name()),
                  (4, fake.first_name(), fake.last_name()),
                  (5, fake.first_name(), fake.last_name())]
cursor.executemany(
    "INSERT INTO Lecturers (lecturer_id, first_name, last_name) VALUES (?, ?, ?)", lecturers_data)

subjects_data = [(1, 'Mathematics', 1),
                 (2, 'Physics', 2),
                 (3, 'Chemistry', 3),
                 (4, 'Biology', 4),
                 (5, 'History', 5)]
cursor.executemany(
    "INSERT INTO Subjects (subject_id, subject_name, lecturer_id) VALUES (?, ?, ?)", subjects_data)

students_data = []
for _ in range(30):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)
    students_data.append((None, first_name, last_name, group_id))
cursor.executemany(
    "INSERT INTO Students (student_id, first_name, last_name, group_id) VALUES (?, ?, ?, ?)", students_data)

grades_data = []
for student_id in range(1, 31):
    for subject_id in range(1, 6):
        for _ in range(20):
            grade = round(random.uniform(1, 5))
            grade_date = fake.date_this_decade()
            grades_data.append(
                (None, student_id, subject_id, grade, grade_date))
cursor.executemany(
    "INSERT INTO Grades (grade_id, student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?, ?)", grades_data)


conn.commit()
conn.close()
