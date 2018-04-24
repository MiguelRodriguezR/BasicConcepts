--visualizar el nombre, edad, estrato y ciudad de aquellas estudiantes mujeres culla edad
--esta entre 22 y 25 años ordenados por edad descendentemente y estrato

SELECT
	nomalumno,edaalumno,estalumno,ciualumno
FROM 
	alumnos
	WHERE 
		sexalumno='F' and edaalumno>=22 and edaalumno<=25
ORDER BY 
	edaalumno desc , estalumno
;

-- otre forma

SELECT
	nomalumno,edaalumno,estalumno,ciualumno
FROM 
	alumnos
	WHERE 
		sexalumno='F' and edaalumno between 22 and 25
ORDER BY 
	edaalumno desc , estalumno
;


--visualizar el nombre sexo y la ciudad de aquellas mujeres de pasto e ipiales 
--y de los hombres de cali bogota 
-- ordenados por ciudad sexo y estrato

SELECT 
	nomalumno,sexalumno,ciualumno
FROM 
	alumnos
	WHERE
		(ciualumno in ('Pasto','Ipiales') and sexalumno like 'F')
		or 
		(ciualumno in ('Cali','Bogota') and sexalumno like 'M')
ORDER BY 
	ciualumno,sexalumno,estalumno
;


-- visualizar el nombre, la edad, el estrato y el sexo de aquellas mujeres mayores de 23 años
-- de estratos 1,2 y 3 y hombres menores que 23 años de estratos 4,5,6 ordenados por sexo, edad
-- estrato.


SELECT
	nomalumno,edaalumno,estalumno,sexalumno
FROM
	alumnos
	WHERE
		(sexalumno like 'F' and edaalumno>23 and estalumno in(1,2,3))
		or
		(sexalumno like 'M' and edaalumno<23 and estalumno in(4,5,6))
ORDER BY
	sexalumno,edaalumno,estalumno
;

--====================================================
--============== NATURAL JOIN ========================
--====================================================


-- visualizar los estudiantes que reprovaron la asignatura de bases de datos ordenados desc
-- por nota final


SELECT 
	nomalumno,nommateria,nfinal,estado
FROM
	alumnos NATURAL JOIN notas NATURAL JOIN materias
	WHERE
		(nommateria like '%ase%ato%') and (estado='R')
ORDER BY
	nfinal desc
;

--visualizar las estudiantes cuya edad esta entre los 20 y 25 de la ciudades de pasto,cali y bogota
--que pertenecen a la facultad de ingenieria, ordenadas por ciudad desc

SELECT 
	nomalumno,edaalumno,ciualumno,nomfacultad
FROM
	alumnos NATURAL JOIN programas NATURAL JOIN facultad
	WHERE
		(sexalumno = 'F' 
		and 
		edaalumno between 20 and 25) 
		and 
		ciualumno in('Pasto','Cali','Bogota')
		and 
		nomfacultad like '%genier%'
ORDER BY
	ciualumno desc
;

--===============================================================================
-- renombrar atributo

alter table alumnos
rename ciudad to ciualumno;

--===============================================================================
-- renombrar una tabla

alter table  alumnos
renaame to tabalumnos;

--=================================================================================
-- cambiar un atributo

update alumnos set 
	sexalumno='M'
WHERE
	codalumno='4600';


-- visualizar los profesores que dictan en medicina organizados por nombre del profesor


SELECT distinct 
	nomprofesor,nomprog
FROM
	profesores NATURAL JOIN notas NATURAL JOIN alumnos NATURAL JOIN programas
	WHERE
		nomprog = 'Medicina'
ORDER BY 
	nomprog
;

-- cuales son los estudiantes de los estratos 2,4 y 6 con materias diferentes a bases de datos 
-- ordenados desc por estrato

SELECT 
	nomalumno,estalumno,nommateria
FROM
	alumnos NATURAL JOIN notas NATURAL JOIN materias
	WHERE 
		estalumno in ('2','4','6') and nommateria not like '%ase%ato%'
ORDER BY
	estalumno desc
;
	 

	

