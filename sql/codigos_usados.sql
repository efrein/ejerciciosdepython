SELECT * FROM `editorial`.`autor` LIMIT 1000;
CREATE TABLE ventas(
    cod         int(11)auto_increment not null,
    descripcion varchar(100) not null,
    valor       decimal(20)not null,
    fecha       date not null,
CONSTRAINT pk_ventas PRIMARY KEY(cod)
);