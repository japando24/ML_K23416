#SELECT * FROM sakila.customer;
select * from customer where store_id=2
#Viet mot cau truy van loc ra cac list of cusmon cos IDCustomer, Name, NumberofRental
SELECT * FROM sakila.customer
    c.customer_id AS CustomerID,
    CONCAT(c.first_name, ' ', c.last_name) AS Name,
    COUNT(r.rental_id) AS NumberOfRental
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY NumberOfRental DESC;
