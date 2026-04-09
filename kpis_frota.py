import pandas as pd

# 1. A Base de Dados Bruta
# Aqui simulamos o sistema da empresa recebendo dados bagunçados de várias viagens.
dados_viagens = {
    'Motorista': ['João', 'Carlos', 'João', 'Ana', 'Carlos'],
    'KM_Rodado': [350, 420, 150, 500, 210],
    'Peso_Transportado_KG': [1200, 3500, 800, 4200, 1500]
}

# 2. Transformando em Tabela
# O Pandas pega esse dicionário e transforma em um DataFrame (que é a versão Python de uma planilha estruturada).
df = pd.DataFrame(dados_viagens)

# 3. O Cálculo dos KPIs (O "Cérebro" do script)
# O comando groupby() junta todas as linhas do mesmo motorista.
# O comando sum() soma o KM e o Peso de cada um deles automaticamente.
kpis_consolidados = df.groupby('Motorista').sum()

# 4. Exibindo o Dashboard no Terminal
print("\n--- Painel de Indicadores de Desempenho (KPIs) da Frota ---")
print(kpis_consolidados)
print("\nProcessamento dos indicadores concluído com sucesso!")