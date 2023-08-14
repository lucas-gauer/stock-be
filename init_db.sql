create database stock;

use stock;

create table products (
    product_id int not null primary key auto_increment,
    name varchar(64) not null,
    stock int not null default 0
);

create table users (
    user_id int not null primary key auto_increment,
    name varchar(64) not null,
    password varchar(255) not null
);
