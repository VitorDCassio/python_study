def executar_robo_faxina():
    import json, csv
    try:
        with open("estoque_portaria.json","r",encoding="utf-8") as portaria:
            dados_portaria = json.load(portaria)
    except(FileNotFoundError) as arquivo_nao_encontrado:
        print("\n---Falha Crítica: Base de dados da portaria não encontrada!---\n")

    veiculos_ativos = []
    historico_finalizados = []

    for dados in dados_portaria:
        if dados["status"]=="Finalizado":
            historico_finalizados.append(dados)
        else:
            veiculos_ativos.append(dados)
    
    with open("estoque_portaria.json", "w") as portaria_atualizada:
        json.dump(veiculos_ativos, portaria_atualizada, indent=4, ensure_ascii=False)
    
    with open("historico_backup.csv", "a", newline="", encoding="utf-8") as backup:
        colunas = ["placa", "fornecedor", "status"]
        escritor = csv.DictWriter(backup,fieldnames=colunas)
        escritor.writerows(historico_finalizados)

executar_robo_faxina()
