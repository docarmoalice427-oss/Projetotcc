SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

DROP DATABASE IF EXISTS almoxarifado;
CREATE DATABASE almoxarifado;
USE almoxarifado;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    quantidade INT NOT NULL,
    foto VARCHAR(500) 
);

INSERT INTO produtos (nome, quantidade, foto) VALUES 
('Chave de Fenda', 15, 'https://exemplo.com'),
('Multímetro Digital', 5, 'https://exemplo.com'),
('Fita Isolante', 50, 'https://exemplo.com');

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(150) NOT NULL UNIQUE, -- Aumentado para suportar e-mails longos sem cortar texto
    senha_hash VARCHAR(255) NOT NULL
);

-- Senha padrão gerada para ambos os e-mails: 1234
INSERT INTO usuarios (usuario, senha_hash) VALUES 
('admin@email.com', '$2b$12$Q6DYJnNAtw66tOCH3wGIdOCrIBaASDijqpYibpQRFVMFXqrg872dS')
