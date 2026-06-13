###Strings
##Cadeia de caracteres, geram palavras e uma cadeia de palavras geram texto!
frase = 'Eu estou aprendendo Python'

###Fatiamento de String - Slice []

##Estrutura
#string[inicio:final:intervalo]
Fatia = frase[9:21:2]

###Analise de String

##Len - Comprimento
#conta quantos carcteres contem a cadeia. Inicia-se a contagem no 0
Comprimento = len(frase) 

##Count - Contar
#conta quantas vezes encontra-se a especificação. Pode-se usar com o slice
Conte = frase.count('o')

##Find - Encontrar
#Encontra a localização onde se inicia a especificação
Encontre = frase.find('Python')
#caso a especificação não exista na frase ela retorna o valo -1, significa "Não existe"
NaoExiste = frase.find('Java')

##(operador) In - Em
#Operador de pergunta se algo consta na string,  retorna True ou False
Pergunta = 'Python' in frase

###Transformação de String

##Replace - Substituir
# Substitui a especificação pelo pedido
frase.replace('Python','Java')

##Upper
#Tudo em MAIÚSCULO
frase.upper()

##Lower
#Tudo em minúsculo
frase.lower()

##Capitalize
#Coloca apenas o primeiro caracter [0] em Maiúsculo
frase.capitalize()

##Title
#Cada palavra começa com Maiúscula
frase.title()

##Strip
#Remove os espaços em branco do inicio e do final. Contem a variação r e l para tratar apenas o lado rigth(direita) e left(esquerda) respectivamente
frase.strip()
frase.rstrip()
frase.lstrip()

###Divisão

##Split
#Cria uma lista onde cada palavra é um elemento
frase.split()

##Join
#"Cola" cada elemento da lista pelo separado definido, gerando uma única string
'-'.join(frase)
