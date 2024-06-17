-- Create users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password_hash TEXT,
    is_author BOOLEAN NOT NULL,
    credits INTEGER DEFAULT 5,  -- New field to track credits
    role TEXT DEFAULT 'regular'  -- New field to indicate role
);

-- Create quizzes table
CREATE TABLE IF NOT EXISTS quizzes (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,  -- Foreign key to reference the author
    is_published BOOLEAN DEFAULT FALSE,  -- Field to indicate if the quiz is published
    is_closed BOOLEAN DEFAULT FALSE,  -- Field to indicate if the quiz is closed
    FOREIGN KEY (author_id) REFERENCES users(id)
);

-- Create questions table
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER NOT NULL,
    text TEXT NOT NULL,
    options TEXT NOT NULL,
    answer TEXT NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
);

-- Create scores table
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    quiz_id INTEGER NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
);