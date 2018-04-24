-- base de datos energia
-- 
create table carfijos(
estrato_car char(1) not null primary key,
valor_car decimal(6,0)
);
--
-- 
create table tarifas(
codigo_tar char(1) not null primary key,
valor_tar decimal(6,0)
);
--

create table barrios(
codigo_ba char(3) not null primary key,
nombre_ba varchar(20),
estrato_ba char(1) not null references carfijos(estrato_car)
);
--
create table usuarios(
codigo_usu char(4) not null primary key,
nombre_usu varchar (20) not null unique,
barrio_usu char(3) not null references barrios(codigo_ba),
sexo_usu char(1)
);
--
create table fabricantes(
cod_fab char(2) not null primary key,
nom_fab varchar(20) not null unique,
pais_fab varchar(20));
--
create table medidores(
codigo_me char(4) not null primary key,
marca_me varchar(20) not null references fabricantes(nom_fab),
digitos_me decimal(2,0),
usuario_me char(4) not null references usuarios(codigo_usu)
);
--
create table lecturas(
medidor char(4) not null primary key references medidores(codigo_me),
lectura_act decimal (6,0) default 0,
lectura_ant decimal (6,0) default 0,
fecha date
);
--
create table facturas(
usuario varchar(20) not null primary key references usuarios(nombre_usu),
kwh decimal (6,0) default 0,
consumo decimal(10,2) default 0,
cargofijo decimal(6,0) default 0,
vrfactura decimal(10,2));
--
-- datos cargos fijos
insert into carfijos values ('1',1000);
insert into carfijos values ('2',2000);
insert into carfijos values ('3',3000);
insert into carfijos values ('4',5000);
insert into carfijos values ('5',10000);
insert into carfijos values ('6',20000);
--
-- datos tarifas
insert into tarifas values ('1',100);
insert into tarifas values ('2',200);
insert into tarifas values ('3',300);
insert into tarifas values ('4',500);
insert into tarifas values ('5',1000);
--
-- datos barrios
insert into barrios values ('B10','La Habana','1');
insert into barrios values ('B11','Lorenzo','2');
insert into barrios values ('B12','Miraflores','3');
insert into barrios values ('B13','San Ignacio','4');
insert into barrios values ('B14','Acacias','5');
insert into barrios values ('B15','Morasurco','6');
insert into barrios values ('B16','Popular','1');
insert into barrios values ('B17','Villa Flor','2');
insert into barrios values ('B18','Santa Monica','3');
--
-- datos usuarios
insert into usuarios values ('1000','P edro Ortiz','B15','M');
insert into usuarios values ('2000','Julio Bucheli','B14','M');
insert into usuarios values ('3000','Sofia Montenegro','B13','F');
insert into usuarios values ('4000','Carmen Casas','B12','F');
insert into usuarios values ('5000','Enrique Pianda','B11','M');
insert into usuarios values ('6000','Camilo Perdomo','B10','M');
insert into usuarios values ('1500','Omar Arevalo','B15','M');
insert into usuarios values ('2500','Laura Cordoba','B14','F');
insert into usuarios values ('3500','Carmen Criollo','B13','F');
insert into usuarios values ('4500','Carlos Diaz','B12','M');
insert into usuarios values ('5500','Jesid Garcia','B11','M');
insert into usuarios values ('6500','Andres Luna','B10','M');
insert into usuarios values ('7000','Wilson Caiza','B15','M');
insert into usuarios values ('7500','Eduardo Paz','B14','M');
insert into usuarios values ('8000','Diana Lopez','B13','F');
insert into usuarios values ('8500','Harold Parra','B12','M');
insert into usuarios values ('9000','Viviana Diaz','B11','F');
insert into usuarios values ('9500','Steven Acosta','B10','M');
insert into usuarios values ('1100','Sebastian Basante','B16','M');
insert into usuarios values ('2100','Daniela Chamorro','B17','F');
insert into usuarios values ('3100','Jessica Montilla','B18','F');
insert into usuarios values ('4100','Harold Mideros','B16','M');
--
-- datso fabricnates
insert into fabricantes values ('10','Iskra','RUSIA');
insert into fabricantes values ('20','G&E','ALEMANIA');
insert into fabricantes values ('30','LG','COLOMBIA');
insert into fabricantes values ('40','Hundai','COREA');
insert into fabricantes values ('50','Zharkosi','FRANCIA');
insert into fabricantes values ('60','Argos','COLOMBIA');

--
-- datos medidores
insert into medidores values ('M100','Iskra',3,'1000');
insert into medidores values ('M200','G&E',4,'2000');
insert into medidores values ('M300','LG',5,'3000');
insert into medidores values ('M400','Iskra',3,'4000');
insert into medidores values ('M500','G&E',4,'5000');
insert into medidores values ('M600','LG',5,'6000');
insert into medidores values ('M150','Iskra',3,'1500');
insert into medidores values ('M250','G&E',4,'2500');
insert into medidores values ('M350','LG',5,'3500');
insert into medidores values ('M450','Iskra',3,'4500');
insert into medidores values ('M550','G&E',4,'5500');
insert into medidores values ('M650','LG',5,'6500');
insert into medidores values ('M700','Iskra',3,'7000');
insert into medidores values ('M750','G&E',4,'7500');
insert into medidores values ('M800','LG',5,'8000');
insert into medidores values ('M850','Iskra',3,'8500');
insert into medidores values ('M900','G&E',4,'9000');
insert into medidores values ('M950','LG',5,'9500');
insert into medidores values ('M110','G&E',5,'1100');
insert into medidores values ('M210','Iskra',3,'2100');
insert into medidores values ('M310','Iskra',4,'3100');
insert into medidores values ('M410','G&E',5,'4100');


--
-- datos lecturas
--
insert into lecturas values ('M100',700,100,'01/09/2012');
insert into lecturas values ('M200',300,100,'01/09/2012');
insert into lecturas values ('M300',3000,2000,'01/09/2012');
insert into lecturas values ('M400',500,100,'01/09/2012');
insert into lecturas values ('M500',1000,100,'01/09/2012');
insert into lecturas values ('M600',800,300,'01/09/2012');
insert into lecturas values ('M150',700,100,'01/09/2012');
insert into lecturas values ('M250',300,100,'01/09/2012');
insert into lecturas values ('M350',3000,2000,'01/09/2012');
insert into lecturas values ('M450',500,100,'01/09/2012');
insert into lecturas values ('M550',1000,100,'01/09/2012');
insert into lecturas values ('M650',800,300,'01/09/2012');
insert into lecturas values ('M700',700,100,'01/09/2012');
insert into lecturas values ('M750',300,100,'01/09/2012');
insert into lecturas values ('M800',3000,2000,'01/09/2012');
insert into lecturas values ('M850',500,100,'01/09/2012');
insert into lecturas values ('M900',1000,100,'01/09/2012');
insert into lecturas values ('M950',800,300,'01/09/2012');


-- 
-- facturas
--
insert into facturas values ('Pedro Ortiz',600,60000,20000,80000);
insert into facturas values ('Julio Bucheli',200,20000,10000,30000);
insert into facturas values ('Sofia Montenegro',1000,10000,5000,105000);
insert into facturas values ('Carmen Casas',400,40000,3000,43000);
insert into facturas values ('Enrique Pianda',900,90000,2000,92000);
insert into facturas values ('Camilo Perdomo',500,50000,1000,51000);
insert into facturas values ('Omar Arevalo',600,60000,20000,80000);
insert into facturas values ('Laura Cordoba',200,20000,10000,30000);
insert into facturas values ('Carmen Criollo',1000,10000,5000,105000);
insert into facturas values ('Carlos Diaz',400,40000,3000,43000);
insert into facturas values ('Jesid Garcia',900,90000,2000,92000);
insert into facturas values ('Andres Luna',500,50000,1000,51000);
insert into facturas values ('Wilson Caiza',600,60000,20000,80000);
insert into facturas values ('Eduardo Paz',200,20000,10000,30000);


/*
1. Crear la base de datos energia y el usuario energiaXX y como este usuario   ejecutar este script

2. Realizar las siguientes consultas:
1.sql.  A cuales usuarios de estratos 1,2 y 3 con medidores marcas ISKRA Y G&E todavia no se le han tomado lecturas, ordenados por estrato y medidor (10 puntos).

2.sql.Cuales usuarios hombres con medidores importados de estratos 2 y 4 consumen mas kwh que los usuarios mujeres con medidores colombianos de estratos 3,4 y 5, ordenados por sexo y kwh (10 puntos).

3.sql.  A Cuales barrios no les han instalado medidores colombianos, ordenados por barrios. (10 puntos).

4.sql.Cuales son los usuarios del mismo estrato que pagan el mismo valor de la factura, ordenados por usuarios. No debe aparecer el mismo usuario (10 puntos).

5.sql.Cuales fabricantes no han vendido medidores en los barrios 'Lorenzo','Miraflores','San Ignacio' y 'Acacias'   


!!!Exitos

*/
 



 
