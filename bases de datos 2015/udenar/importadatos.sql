-- importa datos
-- borrando datos 
delete from tabnotas;
delete from tabalumnos;
delete from tabprogramas;
--
copy tabprogramas from '/home/septimob03/udenar/programas.dat' delimiters',';
select * from tabprogramas;
--
copy tabalumnos from '/home/septimob03/udenar/alumnos.dat' delimiters',';
select * from tabalumnos;
--
copy tabnotas(codalumno,codmateria,codprofesor,parcial1,parcial2,efinal) from '/home/septimob03/udenar/notas.dat' delimiters',';
select * from tabnotas;
--
copy tabalumnos from '/home/septimob03/udenar/alumnos1.dat' delimiters',';
select * from tabalumnos;
--
copy tabnotas(codalumno,codmateria,codprofesor,parcial1,parcial2,efinal) from '/home/septimob03/udenar/notas1.dat' delimiters',';
select * from tabnotas;
