print('''Desafio 022
Crie um programa que leia o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
''')

nome = input("Digite seu nome completo: ")

print(f"Seu nome em maiúsculo é: {nome.upper()}")

print(f"Seu nome em minúsculo é: {nome.lower()}")

dividinome = nome.split()
nomeSemEspaço = "".join(dividinome)
print(f"Seu nome tem {len(nomeSemEspaço)} letras")

print(f'Seu primeiro nome tem {len(dividinome[0])} letras')

print(f'\nConcluido com sucesso')