-- Write a script that prints the full description of the table books from the database alx_book_store in your MySQL server.
-- Ensure that the database is created if it does not already exist.
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

SHOW CREATE TABLE Books;

SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'Books';
