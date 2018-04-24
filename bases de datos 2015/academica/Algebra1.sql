--visualisar el nombre, la edad, el sexo,
--y la ciudad de los estudiantes de la ciudad de 
--Pasto Ipiales y tumaco ordenados por ciudad, sexo y edad

SELECT nomalumno,edaalumno,sexalumno,ciualumno 
	FROM alumnos 
		WHERE 
			ciualumno like 'Pasto' or 
			ciualumno like 'Ipiales' or 
			ciualumno like 'Tumaco'
ORDER BY (ciualumno,sexalumno,edaalumno);

-- OTRA FORMA

SELECT nomalumno,edaalumno,sexalumno,ciualumno 
	FROM alumnos 
		WHERE 
			ciualumno in ('Pasto','Ipiales','Tumaco')
ORDER BY (ciualumno,sexalumno,edaalumno);

--visualisar el nombre edad estrato y ciudad 
--de aquellas estudiantes mujeres cuya edad esta entre
--22 y 25 años ordenados decendentemente y estrato

SELECT nomalumno,edaalumno,estalumno,ciualumno 
	FROM alumnos 
		WHERE
			sexalumno='F' and 
			edaalumno>=22 and 
			edaalumno<=25 
ORDER BY edaalumno desc,estalumno;

-- OTRA FORMA

SELECT nomalumno,edaalumno,estalumno,ciualumno 
	FROM alumnos 
		WHERE
			sexalumno='F' and 
			edaalumno between 22 and 25 
ORDER BY edaalumno desc,estalumno;
