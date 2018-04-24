select marca_me, nombre_ba from 
barrios join usuarios on barrio_usu=codigo_ba 
join medidores on codigo_usu=usuario_me 
join fabricantes on marca_me=nom_fab
except
select marca_me, nombre_ba from 
barrios join usuarios on barrio_usu=codigo_ba 
join medidores on codigo_usu=usuario_me 
join fabricantes on marca_me=nom_fab
where nombre_ba like 'Lorenzo' or nombre_ba like 'Miraflores' or nombre_ba like 'San Ignacio' or nombre_ba like 'Acacias';
