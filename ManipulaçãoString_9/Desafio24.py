print('''
Desafio 24
    
Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com o nome "SANTO"
''')

cidade = input('Digite o nome de sua cidade: ').upper().split()

print(cidade[0] == 'SANTO')