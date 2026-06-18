

USE sakila;
SELECT 
    f.film_id,
    f.title,
    f.rental_rate,
    c.name AS category,
    COUNT(r.rental_id) AS total_rentals,
    AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_days,
    DAYOFWEEK(r.rental_date) AS dia_semana,
    MONTH(r.rental_date) AS mes
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
LEFT JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.rental_date IS NOT NULL
GROUP BY f.film_id, f.title, f.rental_rate, c.name, DAYOFWEEK(r.rental_date), MONTH(r.rental_date);
