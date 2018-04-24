--importacion datos
--con archivos planos
--como postgres <f2>
--
--importa programas
copy programas from '/home/miguel/Downloads/academica/programas.dat' delimiters ',';
select * from programas;
--importa alumnos
copy alumnos from '/home/miguel/Downloads/academica/alumnos.dat' delimiters ',';
select * from alumnos;
--importa notas
copy notas (codalumno,codmateria,codprofesor,parcial1,parcial2,efinal)
	from '/home/miguel/Downloads/academica/notas.dat' delimiters ',';
select * from notas;
