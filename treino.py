radares = [
    {"placa": "RX-111", "multas": 5},
    {"placa": "BR-222", "multas": 2},
    {"placa": "SP-333", "multas": 8}
]

piores_motoristas = sorted(radares, key=lambda x:x["multas"], reverse=True)
print(piores_motoristas)