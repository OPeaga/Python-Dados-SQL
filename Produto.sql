create database estoque;

use estoque;

create table Produto(
  id int not null auto_increment primary key,
  codigo int not null,
  nome varchar(255) not null,
  descricao varchar(255) not null,
  preco double(5,2) not null,
  categoria varchar(255) not null
);