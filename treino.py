def calcular_tesouro(saque_navio1,saque_navio2,):
    saque_total = saque_navio1 + saque_navio2
    return saque_total

total_ouro_jack = calcular_tesouro(850,1250)
print(f"O Capitão Jack Sparrow roubou um total de {total_ouro_jack} moedas de ouro!")
