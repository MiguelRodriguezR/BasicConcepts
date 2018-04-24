select t1.codigo_usu,t1.nombre_usu,t1.sexo_usu,t1.estrato_ba,t1.pais_fab,t1.consumo,t1.kwh,
t2.codigo_usu,t2.nombre_usu,t2.sexo_usu,t2.estrato_ba,t2.pais_fab,t2.consumo,t2.kwh from
(usuarios join barrios on barrio_usu=codigo_ba
join medidores on codigo_usu=usuario_me 
join lecturas on codigo_me=medidor
join fabricantes on marca_me=nom_fab
join facturas on nombre_usu=usuario)t1
join
(usuarios join barrios on barrio_usu=codigo_ba
join medidores on codigo_usu=usuario_me 
join lecturas on codigo_me=medidor
join fabricantes on marca_me=nom_fab
join facturas on nombre_usu=usuario)t2
on t1.consumo>t2.consumo	
where 
t1.sexo_usu like 'M' and t1.pais_fab not like 'COLOMBIA' 
and (t1.estrato_ba like '2' or t1.estrato_ba like '4') 
and t2.sexo_usu like 'F'
and t2.pais_fab like 'COLOMBIA'
and (t2.estrato_ba like '3' or t2.estrato_ba like '4' or t2.estrato_ba like '5') 
order by t1.sexo_usu,t2.sexo_usu,t1.kwh,t2.kwh;
