# Write your MySQL query statement below

# # This will not work if multiple employee have same max years of exp
# select p.project_id, p.employee_id, max(e.experience_years)
# from Project p
# join Employee e on p.employee_id = e.employee_id
# group by p.project_id;


select x.project_id, x.employee_id
from (
    select p.project_id, p.employee_id, 
    rank() over(partition by p.project_id order by e.experience_years desc) as rnk
    from Project p
    join Employee e on p.employee_id = e.employee_id) x
where x.rnk = 1;










