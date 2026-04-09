'''O Básico de Python'''

#Variáveis e Tipos de Dados
nome = "Alice"      # String
idade = 30          # Inteiro
altura = 1.65       # Float
is_student = True   # Booleano

#Operadores
soma = 10 + 5               # Adição +
subtracao = 10 - 5          # Subtração -
multiplicacao = 10 * 5      # Multiplicação *
divisao = 10 / 5            # Divisão /
modulo = 10 % 3             # Módulo %
exponenciacao = 2 ** 3      # Exponenciação ** 
divisao_inteira = 10 // 3   # Divisão inteira //
igualdade = (10 == 5)       # Igualdade ==
diferenca = (10 != 5)       # Diferença !=
maior_que = (10 > 5)        # Maior que >
menor_que = (10 < 5)        # Menor que <
maior_igual = (10 >= 5)     # Maior ou igual >=
menor_igual = (10 <= 5)     # Menor ou igual <=

'''Estruturas de Dados'''

#Listas []
frutas = ["maçã", "banana", "laranja", "uva"]
#Tuplas ()
coordenadas = (10.0, 20.0)
#Dicionários {}
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
#Sets {}
numeros = {1, 2, 3, 4, 5}

'''Fluxo de Controle'''

##Condicionais

#If     ('SE' verdade)
if nome == 'Alice':
    print(f'Bem vinda, {nome}')
#Elif   ('SENÃO SE' se if for falso elif verdade)
elif nome == 'Vitor':
    print('Acesso bloqueado!')
#Else   ('SENÃO' se if e elif falso else)
else:
    print('Você não tem permissão para acessar')

##Laços de repetição
lista_alunos = ["Alice", "Bob", "Charlie"]
bateria = 100
#For (Para cada)
for aluno in lista_alunos:
    print(f'bem vindo, {aluno}')

for numero in range(5):
    print(numero)

#While (Enquanto)
while bateria > 0:
    'bateria carregada'

#intruções de interrupção para Laços de repetição
    
    #break (Quebrar, parar imediatamente)
    break

    #continue (Interrompe rodada/iteração atual, momentanêa, pula um)
    continue

'''Funções'''

#def e return -> def (definir função) e return (retornar valor)    
def somar_numeros(a, b): # 'a' e 'b' são os funis onde entram os dados, os parâmetros da função - input
    resultado = a + b    # Processamento - o que a função faz com os dados
    return resultado     # Entrega do produto final - output
    
    # Usando a máquina:
meu_calculo = somar_numeros(10, 5) # O Python devolve 15 e guarda na variável

###tipos de argumentos

## Default Arguments - um valor padrão, se não for fornecido outro valor, ele usará o valor padrão
def saudacao(nome, mensagem="Olá"):
    print(f'{mensagem}, {nome}!')

## ARGUMENTOS ARBITRÁRIOS - permite que uma função aceite um número arbitrário de argumentos

# *args (argumentos posicionais) - permite passar um número variável de argumentos posicionais para 
# uma função. Os argumentos são acessados como uma tupla dentro da função.
def imprimir_nomes(*args):
    for nome in args:
        print(nome)
# Exemplo de uso:
imprimir_nomes("Alice", "Bob", "Charlie")  # Isso vai imprimir os nomes um por um

# **kwargs (argumentos nomeados) - permite passar um número variável de argumentos nomeados para
# uma função. Os argumentos são acessados como um dicionário dentro da função.
def imprimir_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')
# Exemplo de uso:
imprimir_informacoes(nome="Alice", idade=30, cidade="São Paulo")  # Isso vai imprimir as informações no formato chave: valor

#Por que usar *args e **kwargs? Porque eles permitem que a função seja mais flexível e possa aceitar um número variável de argumentos, 
# tornando-a mais versátil e reutilizável em diferentes situações, sem a necessidade de definir um número fixo de parâmetros.

###Escopo de Variáveis

##Escopo Local - Variáveis definidas dentro de uma função, só existem dentro dessa função
def minha_funcao():
    variavel_local = "Eu sou local"
    print(variavel_local)

##Escopo Global - Variáveis definidas fora de qualquer função, existem em todo o programa
variavel_global = "Eu sou global"

###Expressões Lambda - Funções anônimas, usadas para criar funções pequenas e simples de forma concisa, sem a necessidade de definir 
# uma função completa usando def. A sintaxe é: 
# lambda argumentos: expressão. A expressão é avaliada e retornada quando a função lambda é chamada. Por exemplo, uma função lambda 
# para somar dois números seria: lambda x, y: x + y. As expressões lambda são úteis para criar funções rápidas e simples, especialmente 
# quando usadas em conjunto com funções de ordem superior, como map(), filter() e sorted().
soma = lambda x, y: x + y
resultado = soma(10, 5) # resultado é 15

'''Erros, Exceções e Arquivos'''

##Erros e Exceções - Situações inesperadas que podem ocorrer durante a execução do programa, como erros de sintaxe, erros de tipo, erros de valor, etc.

#try (Tentar) e except (Exceto) - Blocos de código para lidar com erros e exceções
try:
    resultado = 10 / 0  # Isso vai causar um erro de divisão por zero
except ZeroDivisionError:
    print("Não é possível dividir por zero!")

    ##lista de alguns tipos erros
    # ZeroDivisionError: Ocorre quando se tenta dividir um número por zero.
    # TypeError: Ocorre quando uma operação ou função é aplicada a um objeto de um tipo inadequado.
    # ValueError: Ocorre quando uma função recebe um argumento com um tipo correto, mas um valor inapropriado.
    # IndexError: Ocorre quando se tenta acessar um índice que está fora do intervalo de uma sequência (como uma lista ou tupla).
    # KeyError: Ocorre quando se tenta acessar uma chave que não existe em um dicionário.
    # FileNotFoundError: Ocorre quando se tenta abrir um arquivo que não existe.
    # ImportError: Ocorre quando um módulo ou uma função não pode ser importado.
    # AttributeError: Ocorre quando se tenta acessar um atributo ou método que não existe em um objeto.
    # SyntaxError: Ocorre quando há um erro de sintaxe no código, como um parêntese ou aspas não fechados.
    # NameError: Ocorre quando se tenta usar uma variável que não foi definida.
    # IndentationError: Ocorre quando a indentação do código está incorreta, como misturar espaços e tabulações.
    # MemoryError: Ocorre quando o programa fica sem memória para alocar novos objetos.
    # OverflowError: Ocorre quando o resultado de uma operação é muito grande para ser representado.

#raise (Levantar) - Usado para levantar uma exceção manualmente
def dividir(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero!")
    return a / b

'''Manipulação de Arquivos - Abrir, ler, escrever e fechar arquivos'''

#open() - Função para abrir um arquivo
arquivo = open('meu_arquivo.txt', 'r')  # 'r' para leitura

#read() - Método para ler o conteúdo de um arquivo
conteudo = arquivo.read()

#write() - Método para escrever em um arquivo
arquivo_escrita = open('meu_arquivo.txt', 'w')  # 'w' para escrita
arquivo_escrita.write("Olá, mundo!")

#close() - Método para fechar um arquivo
arquivo.close()
arquivo_escrita.close()

#with - Gerenciador de contexto para manipulação de arquivos, garante que o arquivo seja fechado automaticamente após o uso, mesmo que ocorra um erro durante a manipulação 
# do arquivo. Por exemplo, usando with para ler um arquivo:
with open('meu_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()

'''Programação Orientada a Objetos - POO'''

#Class (Classes) - Molde para criar objetos, define atributos e métodos
class Pessoa:
    def __init__(self, nome, idade):  # Método construtor para inicializar os atributos
        self.nome = nome
        self.idade = idade

    def apresentar(self):  # Método para apresentar a pessoa
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

#Object (Objetos) - Instâncias de uma classe, possuem atributos e métodos definidos pela classe. É o ato de "fabricar" o dado real a partir do molde da classe 
usuario = Pessoa("Alice", 30)
usuario.apresentar()  # Chama o método apresentar do objeto usuario

#Atributos - Características ou propriedades de uma classe ou objeto. Por exemplo, na classe 'Pessoa', os atributos são 
# 'nome' e 'idade', que armazenam informações sobre a pessoa.
##instância - O ato de criar um objeto a partir de uma classe, ou seja, a criação de um dado real a partir do molde da 
# classe. Por exemplo, quando criamos o objeto 'usuario' a partir da classe 'Pessoa', estamos criando uma instância 
# da classe 'Pessoa'.

class Contador:
    contagem = 0  # Atributo para contar o número de instâncias

    def __init__(self):
        Contador.contagem += 1  # Incrementa a contagem toda vez que uma nova instância é criada
contador1 = Contador()
contador2 = Contador()
print(Contador.contagem)  # Imprime o número de instâncias criadas, que é 2

##Métodos mágicos - Métodos especiais que começam e terminam com dois underlines (__), usados para definir comportamentos 
## específicos de uma classe, como representação, comparação, etc. Alguns exemplos de métodos mágicos incluem:
#__str__(self) - Método mágico para definir a representação em string de um objeto
#__eq__(self, other) - Método mágico para definir a comparação de igualdade entre objetos
#__init__(self, ...) - Método mágico para inicializar os atributos de um objeto quando ele é criado (construtor)
#__len__(self) - Método mágico para definir o comportamento da função len() para um objeto
#__getitem__(self, key) - Método mágico para definir o comportamento de acesso a itens de um objeto usando colchetes []
#__setitem__(self, key, value) - Método mágico para definir o comportamento de atribuição de itens de um objeto usando colchetes []
#__delitem__(self, key) - Método mágico para definir o comportamento de exclusão de itens de um objeto usando colchetes []
#__iter__(self) - Método mágico para definir o comportamento de iteração de um objeto, permitindo que ele seja usado em loops for
#__call__(self, ...) - Método mágico para definir o comportamento de chamada de um objeto como se fosse uma função
#__enter__(self) e __exit__(self, exc_type, exc_value, traceback) - Métodos mágicos para definir o comportamento de um objeto em um gerenciador de contexto (usado com a palavra-chave with)

#O que sao as palavras entre parenteses nos metodos mágicos? 
##Elas são os parâmetros que o método mágico recebe. 
# Por exemplo, no método __str__(self), o parâmetro 'self' é uma referência ao próprio objeto, permitindo que o 
# método acesse os atributos do objeto para criar uma representação em string. Em outros métodos mágicos, 
# como __eq__(self, other), o parâmetro 'other' é uma referência a outro objeto com o qual o objeto atual está 
# sendo comparado. Esses parâmetros permitem que os métodos mágicos definam comportamentos específicos para os 
# objetos de uma classe.

#Métodos - Funções definidas dentro de uma classe, que operam sobre os atributos da classe e definem o comportamento dos 
# objetos criados a partir da classe. Por exemplo, o método 'apresentar' na classe 'Pessoa' é um método que permite que os 
# objetos da classe 'Pessoa' se apresentem.

#Herança - Mecanismo que permite criar uma nova classe (classe filha) a partir de uma classe existente (classe pai), 
# herdando seus atributos e métodos, e podendo adicionar novos ou modificar os existentes.
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        pass  # Método abstrato, será implementado nas classes filhas
class Cachorro(Animal):
    def falar(self):
        return f"{self.nome} late: Au au!"
class Gato(Animal):
    def falar(self):
        return f"{self.nome} mia: Miau!"
cachorro = Cachorro("Rex")
gato = Gato("Mimi")
print(cachorro.falar())  # Output: Rex late: Au au!
print(gato.falar())      # Output: Mimi mia: Miau! 

#Herança Múltipla - Mecanismo que permite criar uma nova classe a partir de múltiplas classes pai, herdando atributos e 
# métodos de todas elas.
class A:
    def metodo_a(self):
        return "Método A"
class B:
    def metodo_b(self):
        return "Método B"
class C(A, B):
    def metodo_c(self):
        return "Método C"
objeto = C()
print(objeto.metodo_a())  # Output: Método A
print(objeto.metodo_b())  # Output: Método B
print(objeto.metodo_c())  # Output: Método C   

#Polimorfismo - Capacidade de objetos de diferentes classes responderem a métodos com o mesmo nome, permitindo 
# que o mesmo método tenha comportamentos diferentes dependendo do objeto que o chama.
class Ave:
    def falar(self):
        return "A ave faz um som"
class Papagaio(Ave):
    def falar(self):
        return "O papagaio fala: Olá!"
class Coruja(Ave):
    def falar(self):
        return "A coruja faz: Hoo hoo!"
ave1 = Papagaio()
ave2 = Coruja()
print(ave1.falar())  # Output: O papagaio fala: Olá!
print(ave2.falar())  # Output: A coruja faz: Hoo hoo!

#Encapsulamento - Princípio de ocultar os detalhes internos de uma classe e expor apenas o necessário para o uso externo,
# geralmente usando métodos públicos para acessar e modificar atributos privados.
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado - identificado por underline duplo (__) - não pode ser acessado diretamente de fora da classe

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.__saldo}")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def consultar_saldo(self):
        return f"Saldo atual: R${self.__saldo}"
conta = ContaBancaria("Alice", 1000)
conta.depositar(500)  # Depósito de R$500 realizado. Saldo atual: R$1500
conta.sacar(200)      # Saque de R$200 realizado. Saldo atual: R$1300
print(conta.consultar_saldo())  # Saldo atual: R$1300

#Abstração - Princípio de simplificar a complexidade de um sistema, expondo apenas os detalhes essenciais e ocultando os 
# detalhes desnecessários.
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        return f"O {self.marca} {self.modelo} está ligado."

    def desligar(self):
        return f"O {self.marca} {self.modelo} está desligado."
carro = Carro("Toyota", "Corolla")
print(carro.ligar())    # Output: O Toyota Corolla está ligado.
print(carro.desligar()) # Output: O Toyota Corolla está desligado.  

'''Conceitos Avançados'''

##Modulos - São arquivos Python que contêm código reutilizável, como funções, classes e variáveis.
# Usamos a palavra reservada import para importar um módulo e acessar suas funcionalidades. Por exemplo, 
# import math para usar funções matemáticas.

##Pacotes - São diretórios que contêm módulos relacionados, organizando o código em uma estrutura hierárquica.
# pip é um gerenciador de pacotes para Python, usado para instalar e gerenciar bibliotecas e dependências 
# de projetos Python. Usamos a palavra reservada import para importar um pacote e acessar seus módulos e funcionalidades. 
# Por exemplo, import numpy para usar a biblioteca de manipulação de arrays e funções matemáticas avançadas.

##Ambientes Virtuais - São ambientes isolados que permitem gerenciar dependências e versões de pacotes para projetos Python, 
# evitando conflitos entre projetos diferentes. Usamos a ferramenta venv para criar e gerenciar ambientes virtuais. 
# Por exemplo, python -m venv meu_ambiente para criar um ambiente virtual chamado "meu_ambiente". Então, podemos ativar o 
# ambiente virtual e instalar pacotes específicos para esse projeto sem afetar outros projetos.

##Compreensão de Listas (List Comprehensions) - Sintaxe concisa para criar listas a partir de iteráveis, usando uma 
# expressão e um loop for. É uma forma ultrarrápida e concisa de criar uma nova lista baseada numa sequência ou 
# lista já existente, compactando um loop inteiro em uma única linha. Por exemplo, [ x**2 for x in range(10) ] cria 
# uma lista de quadrados dos números de 0 a 9.

[x**2 for x in range(10)]  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    ##Modo Lento 
quadrados = [] 
for x in range(5): 
    quadrados.append(x**2) 
        #Por que é mais lento? Porque envolve mais linhas de código, mais operações e mais 
        # chamadas de função (append) do que a compreensão de listas, que é otimizada para criar a 
        # lista em uma única linha.
    
    ##Modo Rápido <- Compreensão de Listas
quadrados = [x**2 for x in range(5)]
        #Por que é mais rápido? Porque a compreensão de listas é implementada em C(linguagem de baixo nível) e 
        # é otimizada para criar a lista em uma única linha, reduzindo o número de operações e chamadas de 
        # função necessárias para criar a lista.
    
    ##sintaxe de compreensão de listas:
    # [expressão for item in iterável if condição]
    # expressão - A operação ou transformação que será aplicada a cada item do iterável.
    # item - A variável que representa cada elemento do iterável durante a iteração.
    # iterável - A sequência ou coleção de elementos que será percorrida, como uma lista, tupla, conjunto, etc.
    # condição (opcional) - Uma expressão que filtra os itens do iterável, permitindo incluir apenas aqueles que satisfazem a condição na nova lista.

##Expressões Regulares - Sequências de caracteres que formam um padrão de pesquisa, usadas para encontrar e manipular 
# texto de forma eficiente. Usamos o módulo re para trabalhar com expressões regulares em Python. Por exemplo, 
# re.search(r'\d+', 'abc123') encontra a primeira sequência de dígitos em uma string. O r antes da string indica que 
# é uma string bruta (raw string), onde as barras invertidas são tratadas literalmente, facilitando a escrita de 
# expressões regulares. 
# Sintaxe de expressões regulares:
# \d - corresponde a qualquer dígito (0-9)
# \w - corresponde a qualquer caractere alfanumérico (letras, dígitos e sublinhado)
# \s - corresponde a qualquer caractere de espaço em branco (espaço, tabulação, nova linha)
# . - corresponde a qualquer caractere, exceto nova linha
# ^ - corresponde ao início da string
# $ - corresponde ao final da string
# * - corresponde a zero ou mais ocorrências do padrão anterior
# + - corresponde a uma ou mais ocorrências do padrão anterior
# ? - corresponde a zero ou uma ocorrência do padrão anterior
# [] - corresponde a qualquer um dos caracteres dentro dos colchetes
# () - agrupa padrões e captura o texto correspondente para uso posterior
# | - corresponde a uma alternativa entre padrões

import re
resultado = re.search(r'\d+', 'abc123')
if resultado:
   print(resultado.group())  # Output: 123

    ##exemplo de expressão regular para validar um endereço de email
email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

#Decoradores - Funções que modificam o comportamento de outras funções ou métodos, permitindo adicionar funcionalidades
# adicionais sem modificar o código original da função ou método.

    ##Exemplo de decorador para medir o tempo de execução de uma função:
    # O termo que é o decorador é o @medir_tempo, que é colocado antes da definição da função calcular_soma para 
    # indicar que a função calcular_soma deve ser decorada com o decorador medir_tempo.
import time
def medir_tempo(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"Tempo de execução: {fim - inicio}")
        return resultado
    return wrapper
@medir_tempo
def calcular_soma(n):
    return sum(range(n))
calcular_soma(1000000)  # Isso vai imprimir o tempo de execução da função calcular_soma

#Geradores - Funções que retornam um iterador, permitindo gerar uma sequência de valores sob demanda, economizando
# memória e melhorando a eficiência em casos de grandes conjuntos de dados ou sequências infinitas.

#Iteradores - Objetos que implementam o protocolo de iteração, permitindo percorrer uma sequência de valores, como listas,
# tuplas, dicionários, etc., usando um loop for ou a função next() para acessar os elementos um por um.

#Context Managers - Estruturas que permitem gerenciar recursos de forma eficiente, garantindo que eles sejam adquiridos e
# liberados corretamente, mesmo em casos de erros ou exceções. Usamos a palavra-chave with para usar um gerenciador de 
# contexto, como no caso de manipulação de arquivos, onde o gerenciador de contexto garante que o arquivo seja 
# fechado automaticamente após o uso, mesmo que ocorra um erro durante a manipulação do arquivo.

'''APIs e Web Services'''

##APIs - Conjunto de regras e protocolos que permitem a comunicação entre diferentes sistemas ou componentes de software,
# permitindo que eles interajam e compartilhem dados de forma eficiente. APIs podem ser usadas para acessar serviços web, 
# bancos de dados, bibliotecas de terceiros, etc., e geralmente são documentadas para facilitar o uso por desenvolvedores.

    #Significado de API - API significa "Application Programming Interface" (Interface de Programação de Aplicações). 
    
    #Consumo de API - O ato de usar uma API para acessar seus recursos e funcionalidades, geralmente por meio de requisições HTTP,
    # para obter dados, enviar dados ou realizar ações específicas. Por exemplo, usar a biblioteca requests para fazer uma requisição 
    # GET a uma API de clima e obter informações sobre o clima atual em uma determinada cidade.

    #Criação de API - O processo de desenvolver uma API para expor recursos e funcionalidades de um sistema ou aplicação, permitindo que
    # outros sistemas ou componentes de software possam interagir com ele. Por exemplo, criar uma API RESTful usando o framework Flask 
    # para permitir que outros desenvolvedores acessem e manipulem dados de um banco de dados de usuários em uma aplicação web.

##Web Services - Serviços disponibilizados na web que permitem a comunicação e troca de dados entre sistemas ou aplicações, geralmente por meio 
# de protocolos como HTTP, SOAP, REST, etc. Web services podem ser usados para integrar sistemas, compartilhar dados, realizar operações remotas, 
# etc., e geralmente são acessados por meio de APIs.

    ##Tipos de Web Services - Existem diferentes tipos de web services, incluindo:
    # SOAP (Simple Object Access Protocol) - Um protocolo de comunicação baseado em XML que define regras para troca de mensagens entre sistemas.
    # REST (Representational State Transfer) - Um estilo arquitetural para desenvolvimento de web services que utiliza HTTP e recursos para 
    #   manipulação de dados.
    # GraphQL - Uma linguagem de consulta para APIs que permite aos clientes solicitar exatamente os dados de que precisam, evitando o excesso 
    #   ou a falta de informações.

##Requisições HTTP - Métodos usados para realizar operações em recursos de uma API ou web service, como GET (obter dados), POST (enviar dados), 
# PUT (atualizar dados), DELETE (excluir dados), etc. As requisições HTTP são usadas para interagir com APIs e web services, permitindo que os 
# clientes acessem e manipulem dados de forma eficiente. Por exemplo, usar a biblioteca requests para fazer uma requisição POST a uma API de 
# cadastro de usuários para criar um novo usuário.
'''import requests
url = 'https://api.exemplo.com/usuarios'
dados = {'nome': 'Alice', 'email': 'alice@example.com'}
response = requests.post(url, json=dados)  
if response.status_code == 201:
    print("Usuário criado com sucesso!")'''

##JSON (JavaScript Object Notation) - Um formato de dados leve e fácil de ler, usado para representar objetos e estruturas de dados em APIs e web services.
#  JSON é amplamente utilizado para troca de dados entre clientes e servidores, permitindo que os dados sejam transmitidos de forma eficiente. Por exemplo,
#  usar a biblioteca json para converter um dicionário Python em uma string JSON antes de enviar uma requisição POST a uma API.
import json
dados = {'nome': 'Alice', 'email': 'alice@example.com'}
dados_json = json.dumps(dados) 
print(dados_json)  # Output: {"nome": "Alice", "email": "alice@example.com"}

##Autenticação e Autorização - Mecanismos usados para garantir a segurança e o controle de acesso em APIs e web services, permitindo que apenas 
# usuários autorizados possam acessar recursos e realizar operações específicas. Autenticação é o processo de verificar a identidade do usuário, 
# enquanto autorização é o processo de verificar se o usuário tem permissão para acessar um recurso ou realizar uma ação específica. Por exemplo, 
# usar tokens de autenticação (como JWT) para proteger uma API e garantir que apenas usuários autenticados possam acessar seus recursos.

##Rate Limiting - Mecanismo usado para controlar a quantidade de requisições que um cliente pode fazer a uma API ou web service em um determinado 
# período de tempo, evitando sobrecarga e garantindo a disponibilidade do serviço para todos os usuários. Por exemplo, uma API pode implementar um 
# limite de 100 requisições por hora para cada cliente, retornando um código de status HTTP 429 (Too Many Requests) quando o limite for excedido.
