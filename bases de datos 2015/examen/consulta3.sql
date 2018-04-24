select distinct t1.nombre_ba from
(usuarios join barrios on barrio_usu=codigo_ba)t1
left join
(usuarios join barrios on barrio_usu=codigo_ba
join medidores on codigo_usu=usuario_me
join fabricantes on marca_me=nom_fab)t2
on t1.codigo_usu=t2.codigo_usu and t2.pais_fab like 'COLOMBIA'
where
t2.pais_fab is NULL
order by t1.nombre_ba;
--
-- OTRA FORMA
--
select nombre_ba from barrios join usuarios on barrio_usu=codigo_ba join medidores on codigo_usu=usuario_me join fabricantes on marca_me=nom_fab
except
select nombre_ba from barrios join usuarios on barrio_usu=codigo_ba join medidores on codigo_usu=usuario_me join fabricantes on marca_me=nom_fab
where pais_fab like '%OLOMB%'
