-- Create the books table
DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(50) NOT NULL,
    pages_num INTEGER NOT NULL,
    review TEXT,
    date_added DATE DEFAULT CURRENT_TIMESTAMP
);

-- Insert data into the books table
INSERT INTO books (title, author, pages_num, review) VALUES
    ('A Tale of Two Cities', 'Charles Dickens', 489, 'A great classic'),
    ('Anna Karenina', 'Leo Tolstoy', 864, 'Another great classic');
