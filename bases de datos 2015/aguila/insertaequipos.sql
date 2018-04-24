-- borrar registros
delete from tabposiciones;
delete from tabequipos;
-- insercion de datos
-- tabla equipos
insert into tabequipos values('10','Deportivo Pasto');
insert into tabequipos values('20','Deportivo Cali');
insert into tabequipos values('30','Nacional');
insert into tabequipos values('40','Millonarios');
-- tabla posiciones
insert into tabposiciones(equipo)values('Deportivo Pasto');
insert into tabposiciones(equipo)values('Deportivo Cali');
insert into tabposiciones(equipo)values('Nacional');
insert into tabposiciones(equipo)values('Millonarios');
