select p.project_id, ROUND(AVG(e.experience_years), 2) as average_years
from project as p
LEFT JOIN employee as e
ON p.employee_id = e.employee_id
group by project_id;