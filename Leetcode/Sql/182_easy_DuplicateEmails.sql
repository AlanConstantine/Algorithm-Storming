-- SQLite

SELECT Email FROM (
SELECT Email, count(Email) as num 
FROM "182_Person" GROUP BY Email
) AS statistic
WHERE num > 1;
-- UPDATE "182_Person" SET Email = "c@d.com" WHERE Id = 2;