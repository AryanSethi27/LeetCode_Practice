select query_name, round(sum(rating/position)/count(position), 2) as quality, 
round(sum(rating<3)/count(position)*100, 2) as poor_query_percentage
from queries
where query_name is NOT NULL
group by query_name