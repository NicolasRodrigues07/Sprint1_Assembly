import time

print("=== Sistema de Autenticação de Carregador EV ===\n")

carro = input("Digite o modelo do seu carro: ")
bateria = int(input("Nível atual da bateria (%): "))

if bateria >= 100:
    print("Bateria já está cheia! Carregamento não necessário.")
else:
    conexao = input("O veículo está conectado ao carregador? (S/N): ").upper()

    if conexao == "S":
        print(f"\n Autenticação concluída!")
        print(f"  Carro: {carro}")
        print(f"  Bateria atual: {bateria}%")
        print(f"  Carregamento iniciado...\n")

        continuar = input("Deseja interromper o carregamento imediatamente? (S/N): ").upper()
        
        if continuar == "S":
            print("Carregamento interrompido pelo usuário. Desconecte o cabo com segurança.")
        else:
            print("\n🔋 Carregando...", end="")
            # Loop que simula o preenchimento da bateria de 1 em 1 segundo
            while bateria < 100:
                bateria += 5  # Aumenta de 5 em 5% para ir mais rápido
                if bateria > 100:
                    bateria = 100
                
                time.sleep(0.5)  # Pausa de 1 segundo para simular o tempo passando
                print(f" [{bateria}%]", end="", flush=True)
            
            # Mensagem de finalização com sucesso
            print(f"\n\n⚡ Carregamento concluído com sucesso!")
            print(f"  O {carro} está pronto para rodar. Pode desconectar o cabo com segurança.")

    elif conexao == "N":
        print("Conexão não detectada. Verifique o cabo e tente novamente.")
    else:
        print("Entrada inválida. Digite S para Sim ou N para Não.")
