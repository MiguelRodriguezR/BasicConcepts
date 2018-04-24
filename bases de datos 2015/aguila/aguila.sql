--aguila.sql
--borrar tabla
drop table tabposiciones;
drop table tabpartidos;
drop table tabjugadores;
drop table tabequipos;
--crear tablas
--tabla tabequipos
create table tabequipos(
codequipo char(2),
nomequipo varchar(20));
--
--tabla jugadores
create table tabjugadores(
codjugador char(4),
nomjugador varchar(20),
equipo char(2));
--
--tabla partidos
create table tabpartidos(
codlocal char(2),
codvisit char(2),
gollocal smallint,
golvisit smallint,
fecha date);
--
--tabla posiciones
create table tabposiciones(
equipo varchar(20),
pj smallint,
pg smallint,
pe smallint,
pp smallint, 
gf smallint,
gc smallint,
gd smallint,
gp decimal(3,1),
puntos smallint);
--
-- llaves primarias
-- tabla equipos
alter table tabequipos add primary key(codequipo); 
--
-- tabla jugadores
alter table tabjugadores add primary key(codjugador);
--
-- tabla partidos
alter table tabpartidos 
add primary key(codlocal,codvisit,fecha);
--
-- tabla posiciones
alter table tabposiciones 
add constraint "equipo_pk" primary key(equipo);
--
-- llaves foraneas
-- tabla posiciones
-- crear indice unico
create unique index "idx_nomequipo" on tabequipos(nomequipo);
-- crear llave foranea
alter table tabposiciones 
add constraint "equipo_fk" foreign key(equipo) references tabequipos(nomequipo);
-- tabla partidos
alter table tabpartidos
add foreign key(codlocal) references tabequipos(codequipo);
--
alter table tabpartidos
add foreign key(codvisit) references tabequipos(codequipo);
--
-- tabla jugadores
alter table tabjugadores
add foreign key(equipo) references tabequipos(codequipo);
-- crear las restricciones-constraints
alter table tabpartidos
alter gollocal set default 0;
--
alter table tabpartidos
alter golvisit set default 0;
--
--tabla posiciones
alter table tabposiciones
alter pj set default 0;
--
alter table tabposiciones
alter pg set default 0;
--
alter table tabposiciones
alter pe set default 0;
--
alter table tabposiciones
alter pp set default 0;
--
alter table tabposiciones
alter gf set default 0;
--
alter table tabposiciones
alter gc set default 0;
--
alter table tabposiciones
alter gd set default 0;
--
alter table tabposiciones
alter gp set default 0;
--
alter table tabposiciones
alter puntos set default 0;
--
-- check
alter table tabpartidos
add constraint "gollocal.chk1" check(gollocal>=0);
--
alter table tabpartidos
add constraint "golvisit.chk2" check(golvisit>=0);
--

