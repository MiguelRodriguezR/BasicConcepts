copy tabprogramas from '/home/septimob03/udenar/alumnos1.dat' delimiters',';
select * from tabalumnos;

copy tabnotas(codalumno,codmateria,codprofesor,parcial1,parcial2,efinal) from '/home/septimob03/udenar/notas1.dat' delimiters',';
select * from tabnotas;
