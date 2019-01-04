-- 写一个 SQL 查询语句，获取 Employee表中第二高的Salary 。

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- 例如, 上面给出的 Employee 表，查询应该返回 200 作为第二高的Salary。如果没有第二高的Salary，那么查询应该返回 null。

-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+


SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary != (
	SELECT MAX(Salary)
FROM Employee
);