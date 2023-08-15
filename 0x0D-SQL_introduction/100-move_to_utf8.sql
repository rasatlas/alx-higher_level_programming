-- A script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
-- You need to convert all of the following to UTF8:
-- Database hbtn_0c_0
-- Table first_table
-- Field name in first_table
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8
COLLATE utf8_general_ci;

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8
COLLATE utf8_unicode_ci;

ALTER first_table
CHANGE id score name
CHARACTER SET utf8
COLLATE utf8_general_ci;
