/* Creates the database hbtn_0d_usa and the table states in it on your MySQL server. */
-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Create the table
CREATE TABLE IF NOT EXISTS states (
	PRIMARY KEY (id),
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL
);
