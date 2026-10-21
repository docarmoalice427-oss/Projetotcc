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
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL
);

-- HASH REAL E VALIDADO GERADO DIRETAMENTE VIA FLASK-BCRYPT PARA A SENHA: 1234
INSERT INTO usuarios (usuario, senha_hash) VALUES 
('admin', '$2b$12$7kPskB150A6yRE2h3M5DDe2Y06C3EexS7qO2YxV65YjD6EGeObeTq'),
('vivi', '$2b$12$R9OaM1.oZ.26uN836nQZ/.3qXkM7yqK4Qo8p9mP6vW0V6B0vYqFBC');
