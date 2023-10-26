# Open Sqlite3
sqlite3
# Create/Open database
-- Create a new database named 'mydatabase.db'
.open mydatabase.db
# Create table and Perform Queries
-- Create a table named 'kiln'
CREATE TABLE kiln (
    id INTEGER PRIMARY KEY,
    tag TEXT,
    value REAL,
    time DATETIME
);

-- Insert data into the table
INSERT INTO kiln (tag, value, time) VALUES ('tag1', 25, 'e');


-- Query the  table
SELECT * FROM kiln;

# Show all Table
.tables

# Check schema table
PRAGMA talbe_info(table_name)


# Clear all record
