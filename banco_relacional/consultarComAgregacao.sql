-- Selecionar regiao
select
    regiao as 'Região',
    -- Somar a população
    sum(populacao) as Total
from `estados`
-- Agrupar pela regiao
GROUP BY regiao
order by Total desc

-- Média
SELECT avg(populacao) as Total
from `estados`
