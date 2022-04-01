SELECT * FROM `editorial`.`autor` LIMIT 1000;
create database editorial;
use editorial;
 create table libro (id_libro int(20) not null auto_increment primary key,titulo varchar(25) not null, fech_publicacion date not null);
 insert into autor (id_autor, nombre, fech_nacimiento) values ("123456789","luis", 2003-09-12);
 describe libro;
