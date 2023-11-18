# Write your MySQL query statement below

select t.tweet_id
from Tweets t
where CHAR_LENGTH(t.content) > 15;

