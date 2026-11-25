-- Write your query below
with bonus as (
    select employee_id, salary as bonus
    from employees 
    where employee_id % 2 = 1
    and name not like 'M%'
)
select employees.employee_id, coalesce(bonus, 0) as bonus
from employees left join bonus 
on employees.employee_id = bonus.employee_id;