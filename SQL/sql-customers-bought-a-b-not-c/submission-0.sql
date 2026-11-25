-- Write your query below
with customer_products as (
    select customer_id, array_agg(product_name) as products
    from orders
    group by customer_id
)
select customer_id, customer_name
from customers natural join customer_products
where 'A' = ANY(products)
and 'B' = ANY(products)
and 'C' <> ALL(products)
order by customer_name;