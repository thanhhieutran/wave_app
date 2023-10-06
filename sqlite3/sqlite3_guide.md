# Open Sqlite3
sqlite3
# Create new database
-- Create a new database named 'mydatabase.db'
.open mydatabase.db
# Create table and Perform Queries
-- Create a table named 'students'
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
);

-- Insert data into the 'students' table
INSERT INTO students (name, age) VALUES ('Alice', 25);
INSERT INTO students (name, age) VALUES ('Bob', 30);

-- Query the 'students' table
SELECT * FROM students;

# Show all Table
.tables
