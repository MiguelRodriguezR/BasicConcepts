--importacion datos
--con archivos planos
--como postgres <f2>
--
--importa alumnos
  copy alumnos from '/home/miguel/Downloads/academica/alumnos1.dat' delimiters ',';
  select * from alumnos;
--importa notas
  copy notas (codalumno,codmateria,codprofesor,parcial1,parcial2,efinal)
	from '/home/miguel/Downloads/academica/notas1.dat' delimiters ',';
--select * from notas;
