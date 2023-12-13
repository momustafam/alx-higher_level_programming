/* Creates the MySQL server user `user_0d_1`. with all privileges */
-- Create the user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFITED BY 'user_0d_1_pwd';
-- Grant all privileges to the user
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
