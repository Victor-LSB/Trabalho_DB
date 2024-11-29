CREATE DATABASE estoque_mercado;

USE estoque_mercado;

CREATE TABLE Produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    descricao VARCHAR(255)
);

CREATE TABLE Fornecedor (
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    contato VARCHAR(100)
);

CREATE TABLE Entrada (
    id_entrada INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    quantidade INT NOT NULL,
    fk_produto INT NOT NULL,
    fk_fornecedor INT NOT NULL,
    FOREIGN KEY (fk_produto) REFERENCES Produto(id_produto),
    FOREIGN KEY (fk_fornecedor) REFERENCES Fornecedor(id_fornecedor)
);

CREATE TABLE Saida (
    id_saida INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    quantidade INT NOT NULL,
    fk_produto INT NOT NULL,
    FOREIGN KEY (fk_produto) REFERENCES Produto(id_produto)
);

CREATE TABLE Avaria (
    id_avaria INT PRIMARY KEY AUTO_INCREMENT,
    data DATE NOT NULL,
    quantidade INT NOT NULL,
    fk_produto INT NOT NULL,
    FOREIGN KEY (fk_produto) REFERENCES Produto(id_produto)
);

CREATE TABLE Estoque (
    id_estoque INT PRIMARY KEY AUTO_INCREMENT,
    fk_produto INT NOT NULL UNIQUE,
    saldo INT NOT NULL,
    FOREIGN KEY (fk_produto) REFERENCES Produto(id_produto) ON DELETE CASCADE
);

