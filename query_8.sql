SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM Grades as g
JOIN Subjects as s ON g.subject_id = s.subject_id
JOIN Lecturers as l ON s.lecturer_id = l.lecturer_id
WHERE s.lecturer_id = 2
AND s.subject_id = 2;