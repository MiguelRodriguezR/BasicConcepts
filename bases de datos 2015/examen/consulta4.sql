select t1.nombre_usu,t1.vrfactura,t1.estrato_ba,t2.nombre_usu,t2.vrfactura,t2.estrato_ba
 from
(usuarios join barrios on barrio_usu=codigo_ba
join facturas on nombre_usu=usuario)t1
join
(usuarios join barrios on barrio_usu=codigo_ba
join facturas on nombre_usu=usuario)t2
on t1.vrfactura=t2.vrfactura and t1.codigo_usu<>t2.codigo_usu and t1.estrato_ba=t2.estrato_ba
order by t1.nombre_usu,t2.nombre_usu;

