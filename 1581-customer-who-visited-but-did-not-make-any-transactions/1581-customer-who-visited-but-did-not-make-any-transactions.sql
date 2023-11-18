# Write your MySQL query statement below

-- ANS 1

# select v.customer_id, count(*) count_no_trans
# from visits v
# left join transactions t on v.visit_id = t.visit_id
# where t.transaction_id is null
# group by v.customer_id;

-- ANS 2

select v.customer_id, count(*) count_no_trans
from visits v
where v.visit_id not in ( select t.visit_id
from visits
join transactions t on visits.visit_id = t.visit_id)
group by v.customer_id;

