-- Write your query below
with highest as (
    select student_id, max(score) as ms
    from exam_results
    group by student_id
)
select student_id, min(exam_id) as exam_id, ms as score
from exam_results natural join highest
where score = ms
group by student_id, ms
order by student_id;