-- academica
--
--eliminar tablas
drop table notas;
drop table alumnos;
drop table programas;
drop table materias;
drop table profesores;
drop table facultades;
--creacion de tablas
--tabla facultades
create table facultades(
codfacultad char(2) not null primary key,
nomfacultad varchar(20));
--
--tabla materias
create table materias(
codmateria char(2) not null primary key,
nommateria varchar(20));
--tabla profesor
create table profesores(
codprofesor char(2)not null primary key,
nomprofesor varchar(20));
--
--tabla programas
create table programas(
codprograma char(2) not null primary key,
nomprograma varchar(20),
codfacultad char(2) not null references facultades(codfacultad));
--
--tabla estudiantes
create table alumnos(
codalumno char(4) not null primary key,
nomalumno varchar(60),
edaalumno smallint check (edaalumno>=10),
fechalumno date,
ciualumno varchar(20),
sexalumno char(1),
check(sexalumno='F' or sexalumno='M'),
estalumno smallint check(estalumno>=1 and estalumno<=6),
codprograma char(2) not null references programas(codprograma));
--
--tabla notas
create table notas(
codalumno char(4) not null references alumnos (codalumno),
codmateria char (2) not null references materias (codmateria),
codprofesor char(2) not null references profesores (codprofesor),
parcial1 decimal(3,1) check (parcial1 between 0 and 5.0),
parcial2 decimal(3,1) check (parcial2 between 0 and 5.0),
efinal decimal(3,1) check (efinal between 0 and 5.0),
nfinal decimal(3,1),
estado char(1),
primary key (codalumno,codmateria));