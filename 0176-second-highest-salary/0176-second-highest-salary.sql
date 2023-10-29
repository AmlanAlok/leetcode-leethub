# Write your MySQL query statement below

# select count(*) from employee;

# select min(salary) as `SecondHighestSalary`
# from employee
# where salary in (select salary
#                 from employee
#                 order by salary desc
#                 limit 2);
             
# select salary
# from employee
# order by salary desc
# limit 2;

select max(salary) as `SecondHighestSalary`
from employee
where salary < (select max(salary) from employee);