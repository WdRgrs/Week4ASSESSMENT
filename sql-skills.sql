-- Aritst table
INSERT INTO artist (name, artist_id)
VALUES ('Polysics', 276), ('Bonnie Prince Billy', 277), ('Roger Alan Wade', 278);



SELECT * FROM artist
WHERE name ILIKE 'a%'
LIMIT 5;



-- Employee Table
SELECT first_name, last_name FROM employee
WHERE city ILIKE 'Calgary';



SELECT * FROM employee 
WHERE last_name ILIKE 'edwards';

SELECT * FROM employee 
WHERE reports_to = 2;



SELECT COUNT(city) FROM employee
WHERE city ILIKE 'lethbridge';



-- Invoice Table
-- This is the total number of units ordered to USA
SELECT SUM(total) FROM invoice
WHERE billing_country ILIKE 'usa';
-- This is the total number of orders to USA
SELECT * from invoice
WHERE billing_country ILIKE 'usa';



SELECT * FROM invoice
ORDER BY total DESC
LIMIT 1;



SELECT * FROM invoice
WHERE total <= 1;
-- OR
SELECT * FROM invoice
JOIN invoice_line ON invoice_line.invoice_id = invoice.invoice_id
ORDER BY invoice.total * invoice_line.unit_price ASC;



SELECT * FROM invoice
JOIN invoice_line ON invoice_line.invoice_id = invoice.invoice_id
WHERE invoice.total * invoice_line.unit_price > 5;



SELECT count(*) FROM invoice
JOIN invoice_line ON invoice_line.invoice_id = invoice.invoice_id
WHERE invoice.total * invoice_line.unit_price < 5;



SELECT sum(invoice.total * invoice_line.unit_price * invoice_line.quantity) FROM invoice
JOIN invoice_line ON invoice_line.invoice_id = invoice.invoice_id;



-- JOIN QUERIES (VARIOUS TABLES)
SELECT * FROM invoice
JOIN invoice_line ON invoice_line.invoice_id = invoice.invoice_id
WHERE unit_price > .99;



SELECT invoice_date, first_name, last_name, total FROM customer
JOIN invoice ON invoice.customer_id = customer.customer_id;



SELECT customer.first_name"Customer First Name", customer.last_name "Customer Last Name", employee.first_name "Rep First Name", employee.last_name "Rep Last Name" FROM customer
JOIN employee ON employee.employee_id = customer.support_rep_id;



SELECT album.title, artist.name FROM album
JOIN artist ON artist.artist_id = album.artist_id;