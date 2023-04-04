CREATE TABLE employees
(
	first_name varchar(30),
	last_name varchar(30),
	title varchar(50),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(50),
	contact_name varchar(50)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(5),
	employee_id int,
	order_date date,
	ship_city varchar(30)
);