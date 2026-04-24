##atalho para comentar ctrl + k +c ; para descomentar ctrl + k + u

##TREINADO FUNÇÕES 10 de abril 2026

# def calcular_tesouro(saque_navio1,saque_navio2,):
#     saque_total = saque_navio1 + saque_navio2
#     return saque_total


# espanha = int(input("Quanto Jack robou na Espanha?\n"))
# frança = int(input("Quanto Jack robou na França?\n"))

# total_ouro_jack = calcular_tesouro(espanha,frança)
# print(f"O Capitão Jack Sparrow roubou um total de {total_ouro_jack} moedas de ouro!")


##TREINANDO ESCOPO DE VARIAVEIS 11 de abril de 2026

# --- ESCOPO GLOBAL --- (O Sistema Oficial da Associação de Caçadores)
# nivel_cacador = 10 

# def treinar_na_masmorra():
    # # --- ESCOPO LOCAL --- (Dentro da Masmorra de Treinamento)
    # nivel_cacador = 50 
    # print(f"Sistema Local: Dentro da masmorra secreta, o nível do caçador subiu para {nivel_cacador}!")
    # return nivel_cacador

# # 1. O Caçador entra na masmorra
# nivel_cacador = treinar_na_masmorra()

# # 2. O Caçador sai da masmorra e a Associação verifica o nível dele
# print(f"Sistema Oficial: Ao sair da masmorra, a Associação vê que o nível é {nivel_cacador}!")

##DESAFIO

# pontos_grifinoria = 320

# def calcular_pontos_partida(capturou_pomo, gols_marcados):

#     pontos_desta_partida = 0
    
#     pontos_desta_partida = gols_marcados * 10 

#     if capturou_pomo == True:
#         pontos_desta_partida += 150

#     return pontos_desta_partida

# pomo = input("\nDigite Sim ou Não, para: Grifinoria capturou o pomo? ")

# while pomo != "Sim" and "Não":
#         print("Digite exatamente a opção com acento e a primeira letra maiuscula! ")
#         pomo = input("\nDigite Sim ou Não, para: Grifinoria capturou o pomo? ")

# if pomo == "Sim":
#     pomo = True
# elif pomo =="Não":
#     pomo = False

# gols = int(input("\nQuantos gols Grifinoria fez? "))

# ponto_partida = calcular_pontos_partida(pomo,gols)

# print(f"\nPontos adquiridos em parida {ponto_partida}\n")

# pontos_grifinoria += ponto_partida

# print(f"\nA Grifinória terminou o campeonato com {pontos_grifinoria} pontos!")

# print("\n----Fim da Partida----")


## TREINADO FALHAS 11 de abril 2026

# xp_total = 10000

# try:
#     sobreviventes = int(input("\nQuantos caçadores sobreviveram à raid? "))
#     xp = xp_total/ sobreviventes
#     print(f"\nCada caçador recebeu {xp} de XP!")
# except ZeroDivisionError:
#     print("\nFALHA NA RAID: Todos os caçadores pereceram. O XP foi perdido para o vazio da masmorra!")
# finally:
#     print("\n[SISTEMA] Conexão com a Masmorra encerrada. Fechando portal...")

## BACKTRACKING 11 de abril de 2026

# rota = list(range(1,6))

# for ilha in rota: 

#     if ilha == 3:
#         print("\nIlha 3 amaldiçoada! Desviando..")
#         continue

#     if ilha == 9:
#         print("\nTesouro encontrado na Ilha 9!")
#         break
# else:
#     print("\nFim da rota. Nenhum tesouro encontrado.")

# def registrar_membros(nome,*titulos,**estatisticas):

#     print(f"\n--------------------\nCaçador: {nome.upper()}\n--------------------")

#     print("\n----------TÍTULOS----------\n")
#     for titulo in titulos:
#         print(f"Título: {titulo.capitalize()}")

#     print("\n----------ESTATISTICAS----------\n")
#     for atributo,valor in estatisticas.items():
#         print(f"{atributo.capitalize()}: {valor}")
#     print("\n")

# registrar_membros("Sung Jin-Woo","Monarca das Sombras","Caçador Rank S","Matador de Dragões",nivel=150,forca=999,agilidade=850)

# def calcular_dano_critico(dano_base: int, multiplicador_critico: float) -> float:
#     return(dano_base * multiplicador_critico)

# resultado = calcular_dano_critico(100,1.5)
# print(resultado)

# calcular_ataque_combo = lambda forca,agilidade,magia: (forca+agilidade+magia)*2

# Ataque_veloz = calcular_ataque_combo(50,30,20)
# print(f"O dano total do combo foi: {Ataque_veloz}!")

# def avaliar_recruta(nivel: int):

#     if nivel < 20:
#         raise ValueError("Recusa do Sistema: Nível insuficiente para a Guilda Ahjin!")
#     elif nivel > 100:
#         raise TypeError("Nível muito alto! Possível espião das trevas detectado!")
#     else:
#         print("Aprovado! Bem-vindo à Guilda!")

# try:
#     avaliar_recruta(155)
# except (ValueError,TypeError) as erros_de_nivel:
#     print(f"\n[ALERTA VERMELHO]: {erros_de_nivel}")

# try:
#     avaliar_recruta(15)
# except (ValueError,TypeError) as erros_de_nivel:
#     print(f"\n[ALERTA VERMELHO]: {erros_de_nivel}")

# with open("registro_guilda.txt", "w") as livro:
#     livro.write("--- LIVRO DE REGISTROS DA GUILDA AHJIN ---\n Membro Fundador: Sung Jin-Woo | Rank: S\n")

# print("Livro de registros criado com sucesso no HD!")

## TERMINAL DE CADASTRO

# nome_cacador = input("Digite o nome do novo membro: ")
# rank_cacador = input("Digite o Rank do caçador: ")

# with open("registro_guilda.txt", "a") as livro:
#     livro.write(f"Novo Membro: {nome_cacador} | Rank: {rank_cacador}\n")

# print("Membro adicionado ao livro com sucesso!")

# with open("registro_guilda.txt", "r", encoding="utf-8") as livro:
#     for linha in livro:
#         linha_limpa = linha.strip()
#         print(f"[SISTEMA_LEITURA]: {linha_limpa}")

# with open("base_cacadores.csv" , "w") as base:
#     base.write("Nome,Rank,Guilda\n")
#     base.write("Sung Jin-Woo,S,Ahjin\n")
#     base.write("Baek Yoon-Ho,S,Tigre Branco\n")
#     base.write("Yoo Jinho,D,Ahjin\n")

import csv

with open("base_cacadores.csv" , "r") as base:
    tabela = csv.DictReader(base)
    for linha in tabela:
        print(f"Caçador: {linha["Nome"]} | Nível de Ameaça: {linha["Rank"]}")
        


