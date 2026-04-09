import pandas as pd
import matplotlib.pyplot as plt

# 1. Base de Dados Bruta (O fluxo de entrada do seu sistema)
dados_viagens = {
    'Motorista': ['João', 'Carlos', 'João', 'Ana', 'Carlos'],
    'KM_Rodado': [350, 420, 150, 500, 210],
    'Peso_Transportado_KG': [1200, 3500, 800, 4200, 1500]
}

# 2. Motor de Processamento (Pandas agrupa e soma)
df = pd.DataFrame(dados_viagens)
kpis_consolidados = df.groupby('Motorista').sum()

# Imprimimos no terminal apenas para manter o log
print("--- Log de Processamento ---")
print(kpis_consolidados)


# ==========================================
# 3. MOTOR GRÁFICO (MATPLOTLIB)
# ==========================================

# Cria a 'tela' (fig) e o eixo principal (ax1). figsize define a largura e altura da janela.
fig, ax1 = plt.subplots(figsize=(10, 6))

# --- Camada 1: Gráfico de Barras (Peso Transportado) ---
# Usamos barras azuis no eixo esquerdo (ax1) para representar a massa bruta transportada.
ax1.bar(kpis_consolidados.index, kpis_consolidados['Peso_Transportado_KG'], color='royalblue', label='Peso (KG)')
ax1.set_xlabel('Motoristas', fontsize=12, fontweight='bold')
ax1.set_ylabel('Peso Transportado (KG)', color='royalblue', fontsize=12, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='royalblue') # Pinta a régua de números de azul

# --- Camada 2: Gráfico de Linha (KM Rodado com Eixo Gêmeo) ---
# Se colocarmos o KM (ex: 500) no mesmo eixo do Peso (ex: 5000), o KM ficaria invisível.
# ax1.twinx() cria um EIXO SECUNDÁRIO do lado direito da tela, independente, mas sobreposto.
ax2 = ax1.twinx() 
ax2.plot(kpis_consolidados.index, kpis_consolidados['KM_Rodado'], color='darkorange', marker='o', linewidth=3, markersize=8, label='KM Rodado')
ax2.set_ylabel('Quilometragem (KM)', color='darkorange', fontsize=12, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='darkorange') # Pinta a régua da direita de laranja

# --- Design e Acabamento ---
plt.title('Dashboard Operacional: Peso Transportado vs KM Rodado', fontsize=14, fontweight='bold')
ax1.grid(axis='y', linestyle='--', alpha=0.4) # Adiciona linhas de grade suaves no fundo
fig.tight_layout() # Recalcula as margens automaticamente para nenhum texto ficar cortado

# 4. Comando de Renderização
# Isso "pausa" o script e abre a janela do sistema operacional com o gráfico desenhado.
plt.show()