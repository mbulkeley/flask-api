CREATE TABLE IF NOT EXISTS greetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) DEFAULT NULL,
    message VARCHAR(255) NOT NULL
);

-- Insert greetings with optional names
INSERT INTO greetings (name, message) VALUES 
(NULL, 'Welcome to the Flask API!'),
('Alice', 'Hello Alice from the Pi!'),
('Bob', 'This is DevSecOps in action, Bob.');
