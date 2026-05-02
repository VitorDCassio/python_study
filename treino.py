# Nossa fila principal (Lista) contendo as fichas dos caminhões (Dicionários)
patio_havir = [
    {"placa": "BR-101", "fornecedor": "Celulose Alpha", "status": "Aguardando"},
    {"placa": "SP-202", "fornecedor": "Bobinas Omega", "status": "Descarregando"}
]

print("--- INÍCIO DO TURNO ---")
print(patio_havir)
print("\n--- EXECUTANDO OPERAÇÕES ---")

# Escreva os seus códigos do Desafio abaixo desta linha:

patio_havir.append({"placa":"MG-404", "fornecedor":"Embalagens Eco", "status":"Aguardando"})

print(patio_havir[0]["fornecedor"])

patio_havir[0]["status"] = "Descarregando"

patio_havir.pop(1)

print(patio_havir)