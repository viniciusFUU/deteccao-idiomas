create database deteccao_idiomas;
use deteccao_idiomas;

create table idiomas(
	cod_idioma varchar(2) primary key,
    descricao_idioma varchar(50) not null
);

create table texto(
	id_texto int auto_increment primary key,
    texto varchar(255) not null,
    cod_idioma varchar(2),
    foreign key (cod_idioma) references idiomas(cod_idioma)
);

insert into idiomas(cod_idioma, descricao_idioma) values ('EN', 'English');
insert into idiomas(cod_idioma, descricao_idioma) values ('ES', 'Español');
insert into idiomas(cod_idioma, descricao_idioma) values ('PT', 'Português');

INSERT INTO texto (texto, cod_idioma) VALUES ('Hello world', 'EN');
INSERT INTO texto (texto, cod_idioma) VALUES ('Olá mundo!', 'PT');
INSERT INTO texto (texto, cod_idioma) VALUES ('Hola mundo', 'ES');