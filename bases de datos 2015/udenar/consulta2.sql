--Visualizar el nombre,edad, estrato y ciudad de aquellas estudiantes mujeres cuya edad esta entre 22 y 25 años ordenados descendentemente por edad

--select nomalumno,edaalumno,estalumno,ciualumno from tabalumnos
--where sexalumno='F' and (edaalumno>=22 and edaalumno<=25) order by edaalumno desc,estalumno;

-- Otra forma ---
select nomalumno,edaalumno,estalumno,ciualumno from tabalumnos
where sexalumno='F' and edaalumno between 22 and 25 order by edaalumno desc,estalumno;

