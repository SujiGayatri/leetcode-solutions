# Write your MySQL query statement below
select d.name as Department,e.name as Employee,e.salary as Salary from Employee e inner join Department d on e.departmentId=d.id 
join(
    select departmentId,max(salary) as Salary from Employee group by departmentId
) m
on e.departmentId=m.departmentId and e.salary=m.Salary;