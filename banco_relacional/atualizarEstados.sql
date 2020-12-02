-- Atualizar tabela estados
update estados
-- Mudar todos os nomes para maranhão
set nome = 'Maranhão'
-- Só os que tiverem MA em sua linha
where sigla = 'MA'

select nome from estados where sigla = 'MA'

update estados
set nome = 'Paraná', populacao = 11.32
WHERE sigla = 'PR'

select nome, populacao from estados where sigla = 'PR'
