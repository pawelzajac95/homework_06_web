SELECT DISTINCT s.subject_id, s.subject_name
FROM Subjects as s
JOIN Grades as g ON s.subject_id = g.subject_id
JOIN Lecturers as l ON s.lecturer_id = l.lecturer_id
JOIN Students as stu ON g.student_id = stu.student_id
WHERE l.lecturer_id = 4
AND stu.student_id = 17;