select W1.id 
from weather as W1
JOIN weather as W2
ON W1.recordDate = DATE_ADD(W2.recordDate, INTERVAL 1 Day)
where W1.temperature > W2.temperature;