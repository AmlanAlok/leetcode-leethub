# Write your MySQL query statement below

# # To understand the output
# select a.machine_id, a.process_id, a.timestamp, b.timestamp
# from activity a
# join activity b on a.machine_id = b.machine_id and a.process_id = b.process_id
# where a.activity_type = 'end' and b.activity_type = 'start'
# group by a.machine_id;

# # ANS-1
# select a.machine_id, round(avg(a.timestamp - b.timestamp), 3) as processing_time
# from activity a
# join activity b on a.machine_id = b.machine_id and a.process_id = b.process_id
# where a.activity_type = 'end' and b.activity_type = 'start'
# group by a.machine_id;

# ANS-2
select a.machine_id, 
round(sum(case when a.activity_type='start' then a.timestamp*-1 else a.timestamp end)/(select count(distinct a.process_id)), 3) as processing_time
from activity a
group by a.machine_id;