# Write your MySQL query statement below

-- Ans 1
# select a.id as Id
# from weather a
# join weather b on DATEDIFF(a.recordDate, b.recordDate) = 1
# where a.temperature > b.temperature;

-- Ans 2
# select a.id
# from weather a
# join weather b on DATEDIFF(a.recordDate, b.recordDate) = 1
# and a.temperature > b.temperature;

-- Ans 2
select a.id
from weather a, weather b 
where DATEDIFF(a.recordDate, b.recordDate) = 1
and a.temperature > b.temperature;

-- Ans 4
# select a.id as Id
# from weather a, weather b 
# where a.recordDate - b.recordDate = 1
# and a.temperature > b.temperature;