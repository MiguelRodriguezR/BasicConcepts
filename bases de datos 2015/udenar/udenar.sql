--Udenar
--Eliminacion de tablas
drop table tabnotas;
drop table tabalumnos;
drop table tabprogramas;
drop table tabprofesores;
drop table tabfacultades;
drop table tabmaterias;

--
--Creacion de tablas
--Tabla facultades
create table tabfacultades(
	codfacultad char(2) not null primary key,
	nomfacultad varchar(20)
	);
--Tabla materias
create table tabmaterias(
	codmateria char(2) not null primary key,
	nommateria varchar(20)
	);
--Tabla profesores
create table tabprofesores(
	codprofesor char(2) not null primary key,
	nomprofesor varchar(20)	
	);
--Tabla programas
create table tabprogramas(
	codprograma char(2) not null primary key,
	nomprograma varchar(20), 
	codfacultad char(2) not null references tabfacultades(codfacultad)
	);
--Tabla alumnos
create table tabalumnos(
	codalumno char(4) not null primary key,
	nomalumno varchar(20),
	edaalumno smallint check (edaalumno>=10),	
	fechalumno date,
	ciualumno varchar (20),
	sexalumno char(1) check (sexalumno='F'or sexalumno='M'),
	estalumno smallint check (estalumno>=1 and estalumno<=6),
	codprograma char(2) not null references tabprogramas(codprograma)	
	);
--Tabla notas
create table tabnotas(
	codalumno char(4) not null references tabalumnos(codalumno),
	codmateria char(2) not null references tabmaterias(codmateria),
	codprofesor char(2) not null references tabprofesores(codprofesor),
	parcial1 decimal(3,1) check (parcial1 between 0 and 5.0),
	parcial2 decimal(3,1) check (parcial2 between 0 and 5.0),
	efinal decimal(3,1) check (efinal between 0 and 5.0),
	nfinal decimal(3,1),
	estado char(1),
	primary key (codalumno,codmateria)
	);




