# Write your MySQL query statement below


with all_dates as (
    select user_id, visit_date
    from UserVisits
    union
    select user_id, '2021-01-01' as `visit_date`
    from UserVisits),
rnk as (
    select *, 
    rank() over(partition by user_id order by visit_date) as date_rnk
    from all_dates)

select a.user_id, MAX(DATEDIFF(b.visit_date, a.visit_date)) as biggest_window
from rnk a
join rnk b on a.user_id = b.user_id
and b.date_rnk = a.date_rnk + 1
group by a.user_id;




# Failed attempts

# select a.user_id, a.visit_date, b.visit_date, ABS(DATEDIFF(a.visit_date, b.visit_date)) as biggest_window,
# rank() over(partition by a.user_id order by ABS(DATEDIFF(a.visit_date, b.visit_date)) desc) as rnk
# from UserVisits a
# join UserVisits b on a.user_id = b.user_id
# where a.user_id = 1;


# select a.user_id, a.visit_date, b.visit_date, ABS(DATEDIFF(a.visit_date, b.visit_date)) as biggest_window,
# rank() over(partition by a.user_id order by ABS(DATEDIFF(a.visit_date, b.visit_date)) desc) as rnk
# from UserVisits a
# join UserVisits b on a.user_id = b.user_id
# where a.user_id = 1;
