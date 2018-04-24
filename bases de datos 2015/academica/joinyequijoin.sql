--alter table notas rename column codalumno to calumno;
--alter table notas rename column codprofesor to cprofesor; 
--alter table alumnos rename column codprograma to cprograma; 
--alter table programas rename column codfacultad to cfacultad; 


--===========================================================================

-- visualizar los programas donde se dicta la materia base de datos
-- ordenados por programa
select distinct 
	nomprograma,nommateria 
	from 
		programas join alumnos on(codprograma=cprograma)
		join notas on(codalumno=calumno)
		join materias on (cmateria=codmateria)
	where
		nommateria like '%ase%ato%'
	order by 
		nomprograma
;
--===========================================================================

-- visualizar las mujeres que reprobaron base de datos y las mujeres que reprobaron telematica todos ellos
-- mayores de 22 años de las ciudades de pasto, ipiales y tumaco ordenados por materia , ciudad  , sexo y edad


select --distinct
	nomalumno,sexalumno,edaalumno,ciualumno,nommateria,nfinal
	from
		alumnos join notas on(codalumno=calumno)
		join materias on(cmateria=codmateria)
	where
		((sexalumno='F' and nommateria like '%ase%ato%' and estado='R')
		or
		(sexalumno='M' and nommateria like '%elema%' and estado='R'))
		and 
		edaalumno>22
		and
		ciualumno in ('Pasto','Ipiales','Tumaco')
	order by
		nommateria,ciualumno,sexalumno,edaalumno
;

--==============================================================================

-- visualizar cuales patusos del programa de ingenieria de sistemas tienen la misma edad y son del mismo estrato
-- de los ipialeños del programa de ingenieria de sistemas

/*
	select 
		nomalumno as nombre,
		edaalumno as edad,
		sexalumno as sexo,
		ciualumno as ciudad,
		nomprograma as programa
		into pastusos 
		from 
			alumnos join programas on (cprograma=codprograma)
		where 
			ciualumno like 'Pasto'
		order by 
			nomalumno
;



	select 
		nomalumno as name,
		edaalumno as age,
		sexalumno as sex,
		ciualumno as city,
		nomprograma as program
		into ipialenos 
		from 
			alumnos join programas on (cprograma=codprograma)
		where 
			ciualumno like 'Ipiales'
		order by 
			nomalumno
;
*/

select
	nombre, edad, name , age
	from
		pastusos join ipialenos on (edad=age)

	order by 
		edad
;
--=============================================================================
-- visualizar los estudiantes que tienen el mismo estraro que Fernando Solano

select
	t1.nomalumno, t1.estalumno , t2.nomalumno , t2.estalumno
	from 
		alumnos t1 join alumnos t2 on (t1.estalumno=t2.estalumno)
	where 
		t1.nomalumno not like '%nando%' and 
		t2.nomalumno like '%nando%'
	order by
		t1.nomalumno

;
--=============================================================================
-- visualizar los estudiantes que son del mismo programa que Carlos Dominguez


select
	t1.nomalumno, t1.nomprograma , t2.nomalumno , t2.nomprograma
	from
		(alumnos join programas on (cprograma=codprograma)) as t1
		join
		(alumnos join programas on (cprograma=codprograma)) as t2
		on (t1.nomprograma = t2.nomprograma)
	where
		t1.nomalumno not like '%arlo%mingue%' and
		t2.nomalumno like '%arlo%mingue%'
	order by
		t1.nomalumno


