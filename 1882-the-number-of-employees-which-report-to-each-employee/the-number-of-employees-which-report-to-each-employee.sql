select e.reports_to as employee_id, s.name, count(e.employee_id) as reports_count, round(avg(e.age)) as average_age
from Employees e
Left Join Employees s
ON e.reports_to = s.employee_id
group by e.reports_to
Having count(e.reports_to) > 0
order by employee_id