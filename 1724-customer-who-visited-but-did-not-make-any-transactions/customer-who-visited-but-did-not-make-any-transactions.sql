select customer_id, count(v.visit_id) as count_no_trans
from visits as v
LEFT JOIN transactions as t
on v.visit_id = t.visit_id
where t.visit_id is NULL
GROUP BY customer_id;