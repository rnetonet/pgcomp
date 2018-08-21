select distinct modelagem_voto.votacao_id, modelagem_partido.id as partido_id, modelagem_partido.nome, modelagem_voto.opcao, 
	count(*) over (partition by modelagem_voto.votacao_id, modelagem_partido.nome, modelagem_voto.opcao)::float / count(*) over (partition by modelagem_voto.votacao_id, modelagem_partido.nome)::float as percentual
from modelagem_voto
inner join modelagem_parlamentar on
modelagem_voto.parlamentar_id = modelagem_parlamentar.id
inner join modelagem_partido on
modelagem_parlamentar.partido_id = modelagem_partido.id
where votacao_id in (
	select modelagem_votacao.id
	from modelagem_votacao
	inner join modelagem_proposicao on
	modelagem_votacao.proposicao_id = modelagem_proposicao.id
	where 
		modelagem_proposicao.casa_legislativa_id = 23
		and extract('year' from data) = 2017
)
and modelagem_voto.opcao in ('SIM', 'NAO')
order by modelagem_voto.votacao_id, modelagem_partido.nome, modelagem_voto.opcao