--visualizar el nombre, la edad  y el sexo de los estudiantes de las ciudades de Pasto, Ipiales y tumaco ordenados por ciudad sexo y edad

--select nomalumno,edaalumno,sexalumno,ciualumno from tabalumnos 
--where ciualumno like 'Pasto' or ciualumno like 'Ipiales'or ciualumno like 'Tumaco' order by ciualumno,sexalumno,edaalumno;
--
--otra forma ---> la serie de or se puede cambiar por in
select nomalumno,edaalumno,sexalumno,ciualumno from tabalumnos 
where ciualumno in( 'Pasto', 'Ipiales', 'Tumaco') order by ciualumno,sexalumno,edaalumno;
