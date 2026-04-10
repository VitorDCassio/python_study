## 1. Encruzilhadas Lógicas (if / elif / else)

#No Python, o controle de fluxo é ditado pela indentação (os espaços antes do código). 
# Não usamos chaves {}. Se a condição for verdadeira (True), o bloco indentado abaixo 
# dela é executado. O Python avalia de cima para baixo. Assim que ele encontra uma 
# condição verdadeira ele executa aquele bloco e ignora todo o resto.

## 2. Os Domadores de Repetição (for e while)

#O FOR não é aquele contador clássico do C ou Java (for i=0; i<10; i++). Ele é um 
# iterador. Ele "passeia" por dentro de uma coleção de itens (como uma lista ou um 
# intervalo de números). Para gerar números rapidamente, usamos o 
# range(inicio, parada, passo). 
#O WHILE repete um bloco de código enquanto uma condição for verdadeira. 
# Cuidado com os loops infinitos!

for i in range(1,11):
    if i % 2 == 0:
        print(f"{i} é parSith")
    else:
        print(f"{i} é ímpar Jedi")

a = 0
while a < 3:
    print(f"While: {a}")
    a += 1