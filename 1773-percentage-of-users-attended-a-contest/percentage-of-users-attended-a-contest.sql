select contest_id, ROUND(count(user_id)/(select count(user_id) from users)*100, 2) AS percentage
from register
group by contest_id
order by percentage DESC, contest_id ASC;