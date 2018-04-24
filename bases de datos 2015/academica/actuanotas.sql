--actuanot.sql
--actualiza notas
update notas set
nfinal=parcial1*0.30+parcial2*0.30+efinal*0.40;
--actualiza estado
update notas set estado='A' where nfinal>=3.0;
--estado reprobado
update notas set estado='R' where nfinal<3.0;
