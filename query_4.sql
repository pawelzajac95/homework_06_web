SELECT g.group_id, g.group_name, ROUND(AVG(grade), 2) AS average_grade
FROM Grades as gr
JOIN Students as s ON gr.student_id = s.student_id
JOIN Groups as g ON s.group_id = g.group_id
GROUP BY g.group_id, g.group_name;