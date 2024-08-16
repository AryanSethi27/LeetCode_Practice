SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    activity
WHERE 
    activity_date + INTERVAL 30 DAY > '2019-07-27'
    AND activity_date <= '2019-07-27'
GROUP BY 
    activity_date;