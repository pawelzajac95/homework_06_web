SELECT s.student_id, s.first_name, s.last_name, AVG(g.grade) AS average_grade
FROM Students as s
JOIN Grades as g ON s.student_id = g.student_id
GROUP BY s.student_id, s.first_name, s.last_name
ORDER BY average_grade DESC
LIMIT 5;