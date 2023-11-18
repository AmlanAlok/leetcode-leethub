# Write your MySQL query statement below

# select y.unique_id, x.name
# from Employees x
# join EmployeeUNI y on x.id = y.id;

select y.unique_id, x.name
from Employees x
left join EmployeeUNI y on x.id = y.id;