CREATE TABLE IF NOT EXISTS greetings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255)
);

INSERT INTO greetings (message) VALUES 
('Welcome to the Flask API!'),
('Hello from the Pi!'),
('This is DevSecOps in action.');
