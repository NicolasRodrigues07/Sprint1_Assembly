print("=== Sistema de Autenticação de Carregador EV ===\n")

carro = input("Digite o modelo do seu carro: ")
bateria = int(input("Nível atual da bateria (%): "))

if bateria >= 100:
    print("Bateria já está cheia! Carregamento não necessário.")
else:
    conexao = input("O veículo está conectado ao carregador? (S/N): ").upper()

    if conexao == "S":
        print(f"\n✔ Autenticação concluída!")
        print(f"  Carro: {carro}")
        print(f"  Bateria atual: {bateria}%")
        print(f"  Carregamento iniciado...\n")

        continuar = input("Deseja interromper o carregamento? (S/N): ").upper()
        if continuar == "S":
            print("Carregamento interrompido. Desconecte o cabo com segurança.")
        else:
            print(f"Carregando... Notificaremos quando atingir 100%.")

    elif conexao == "N":
        print("Conexão não detectada. Verifique o cabo e tente novamente.")
    else:
        print("Entrada inválida. Digite S para Sim ou N para Não.")