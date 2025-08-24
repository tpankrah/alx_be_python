CREATE DATABASE  alx_book_store;
USE alx_book_store;


CREATE TABLE  IF NOT EXISTS Authors (
    `author_id` INT PRIMARY KEY,
    `author_name` VARCHAR(215)
);

CREATE TABLE IF NOT EXISTS  Books (
    `book_id` INT PRIMARY KEY,
    `title` VARCHAR(130),
    `author_id` INT, 
    `price` DOUBLE,
    `publication_date` DATE,
    FOREIGN KEY (`author_id`) REFERENCES Authors(`author_id`)
   
);


-- Customers: Stores information about customers.
CREATE TABLE IF NOT EXISTS Customers (
    `customer_id`  INT PRIMARY KEY,
    `customer_name` VARCHAR(215),
    `email` VARCHAR(215),
    `address` TEXT
);


-- Orders: Stores information about orders placed by customers.
CREATE TABLE IF NOT EXISTS Orders(
`order_id` INT PRIMARY KEY,
`customer_id` INT,
`order_date` DATE,
FOREIGN KEY (`customer_id`) REFERENCES Customers(`customer_id`)
);
-- Order_Details: Stores information about the books included in each order.

CREATE TABLE IF NOT EXISTS order_details(
`orderdetailid` INT PRIMARY KEY,
`order_id` INT,
`book_id` INT,
`quantity` DOUBLE,
FOREIGN KEY (`order_id`) REFERENCES Orders(`order_id`),
FOREIGN KEY (`book_id`) REFERENCES Books(`book_id`)
);
