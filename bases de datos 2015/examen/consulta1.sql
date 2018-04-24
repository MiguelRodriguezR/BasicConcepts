select * from
(usuarios join barrios on barrio_usu=codigo_ba 
join medidores on codigo_usu=usuario_me)
left join lecturas on codigo_me=medidor
where (estrato_ba like '1' or estrato_ba like '2' or estrato_ba like '3') 
and (marca_me like 'Iskra' or marca_me like 'G&E')
and lectura_act is NULL
order by estrato_ba, marca_me;

