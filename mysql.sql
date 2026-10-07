
CREATE DATABASE IF NOT EXISTS almoxarifado;

USE almoxarifado;

CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL(10, 2) DEFAULT 0.00
);

INSERT INTO produtos (nome, quantidade, preco) VALUES 
('Chave de Fenda', 15, 12.50),
('Multímetro Digital', 5, 89.90),
('Fita Isolante', 50, 4.25);