import pandas as pd
import numpy as np

filename = 'raw_2016.csv'
raw_df = pd.read_csv(filename)

votacoes = raw_df.votacao_id.unique()
partidos = raw_df.nome.unique()

votacoes.sort()
partidos.sort()

df = pd.DataFrame(np.full((len(partidos), len(votacoes)), 0.5), index=partidos, columns=votacoes)
df.index.name = "partido"

for partido in partidos:
    df_votacoes_partido = raw_df[raw_df.nome == partido]
    for votacao in votacoes:
        df_votacao = df_votacoes_partido[df_votacoes_partido.votacao_id == votacao]
        df_abstencao = df_votacao[df_votacao.opcao == 'ABSTENCAO']
        df_obstrucao = df_votacao[df_votacao.opcao == 'OBSTRUCAO']
        df_sim = df_votacao[df_votacao.opcao == 'SIM']
        df_nao = df_votacao[df_votacao.opcao == 'NAO']
        
        sim = 0

        if not df_sim.empty:
            sim += df_sim.iloc[0]['percentual']
        if not df_abstencao.empty:
            sim += df_abstencao.iloc[0]['percentual'] / 2.0
        if not df_obstrucao.empty:
            sim += df_obstrucao.iloc[0]['percentual'] / 2.0

        df.at[partido, votacao] = sim

df.to_csv(filename.replace('raw', 'data'))
print(df)