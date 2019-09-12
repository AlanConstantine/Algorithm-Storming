-- SQLite

SELECT Email FROM (
SELECT Email, count(Email) as num 
FROM "182_Person" GROUP BY Email
) AS statistic
WHERE num > 1;