-- Seleciona todos de estados
select * from estados

-- Selecionar as duas colunas de `estados`
-- Para dar nome a uma coluna se usa o as
select Sigla, nome as 'Nome do estado' from estados
-- Enquanto regiao for = sul então mostra so da regiao sul
where regiao = 'sul'


-- Selecionar as duas colunas de `estados`
select nome, regiao from estados
-- Se a população for maior ou igual 1 10m
-- irá mostrar
where populacao >= 10
-- Ordenar a população de form descrecente
order by populacao desc
