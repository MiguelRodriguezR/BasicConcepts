--actuanot.sql
--actualiza notas
--actualiza NOTA FINAL
update tabnotas set nfinal=parcial1*0.30+parcial2*0.30+efinal*0.40;
--actualiza estado
--estado aprobado
update tabnotas set estado='A'where nfinal>=3.0;
--estado reprobado
update tabnotas set estado='R'where nfinal<3.0;
