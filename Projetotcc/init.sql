SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

DROP DATABASE IF EXISTS almoxarifado;
CREATE DATABASE almoxarifado;
USE almoxarifado;

CREATE TABLE produtos
(   id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    quantidade INT NOT NULL,
    foto VARCHAR(500));

CREATE TABLE usuarios 
(   id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL);

INSERT INTO produtos (nome, quantidade, foto) VALUES 
('Chave de Fenda', 15, 'https://www.madeirasgasometro.com.br/chave-de-fenda-cromo-vanadio-5-16x4pol-vonder/p?srsltid=AYCX9vJdAtIjqjzoJb9t4gH1YC_X7XvEjg9jQ_gBZMl3uSWjYEQB1pJW'),
('Martelo', 13, 'https://www.eletrorastro.com.br/produto/martelo-unha-25mm-cabo-fibra-emborrachado-vonder-89343?srsltid=AYCX9vKWH1TVkV4UW8T-bzXbWWb4caTWguhRqAouK675wWKDpwtciRqv');

-- Senha padrão para o admin: 1234
INSERT INTO usuarios (usuario, senha_hash) VALUES 
('admin@email.com', '$2b$12$Q6DYJnNAtw66tOCH3wGIdOCrIBaASDijqpYibpQRFVMFXqrg872dS');