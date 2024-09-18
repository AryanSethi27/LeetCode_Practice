SELECT e.name, b.bonus
FROM employee as e
LEFT JOIN bonus as b
on e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus is NULL