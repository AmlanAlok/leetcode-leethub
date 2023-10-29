# {"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100]]}}
# {"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100],[2,200],[3,300]]}}
# {"headers":{"Employee":["id","salary"]},"rows":{"Employee":[[1,100],[2,100]]}}
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

# Ans-1
# select max(salary) as `SecondHighestSalary`
# from employee
# where salary < (select max(salary) from employee);


# Ans-2
select min(salary) as `SecondHighestSalary`
from (select salary
    from employee
    group by salary
    order by salary desc
    limit 1
    offset 1) as x;

