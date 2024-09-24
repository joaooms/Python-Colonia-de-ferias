# João Vitor Monteiro
# Programa para calcular o orçamento de estadia em uma colônia de férias para funcionários.

def obter_diaria(tipo_apartamento, quantidade_pessoas):
    """
    Retorna o valor da diária com base no tipo de apartamento e quantidade de pessoas.
    """
    tabela_diarias = {
        1: [20.00, 28.00, 35.00, 42.00, 48.00, 53.00],
        2: [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]
    }
    return tabela_diarias[tipo_apartamento][quantidade_pessoas - 1]

def calcular_orcamento(quantidade_pessoas, tipo_apartamento, periodo):
    """
    Calcula o valor total da diaria.
    """
    diaria = obter_diaria(tipo_apartamento, quantidade_pessoas)
    custo_total = diaria * periodo
    return custo_total

def mostrar_tabela_diarias():
    """
    Exibe a tabela de diárias para os apto.
    """
    print("\nTabela de Diárias:")
    print("Tipo 1: ", [f"R$ {valor:.2f}" for valor in [20.00, 28.00, 35.00, 42.00, 48.00, 53.00]])
    print("Tipo 2: ", [f"R$ {valor:.2f}" for valor in [25.00, 34.00, 42.00, 50.00, 57.00, 63.00]])

def validar_entrada(quantidade_pessoas, tipo_apartamento):
    """
    Valida os dados de entrada fornecidos pelo usuário.
    """
    return 1 <= quantidade_pessoas <= 6 and tipo_apartamento in [1, 2]

def main():
    while True:
        print("\n=== Menu de Opções ===")
        print("1. Calcular Orçamento de Estadia")
        print("2. Visualizar Tabela de Diárias")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                quantidade_pessoas = int(input("Informe quantas pessoas (1 a 6): "))
                tipo_apartamento = int(input("Informe o tipo de apartamento (1 ou 2): "))
                periodo = int(input("Informe quanto tempo de estadia (em dias): "))
                
                if validar_entrada(quantidade_pessoas, tipo_apartamento):
                    custo_total = calcular_orcamento(quantidade_pessoas, tipo_apartamento, periodo)
                    print(f"\nOrçamento total para {quantidade_pessoas} pessoa(s) no apartamento tipo {tipo_apartamento} por {periodo} dias: R$ {custo_total:.2f}")
                else:
                    print("Dados de entrada inválidos. Verifique as informações e tente novamente.")
            except ValueError:
                print("Erro: Por favor, insira valores numéricos válidos.")

        elif opcao == '2':
            mostrar_tabela_diarias()

        elif opcao == '3':
            print("Saindo do programa. Obrigado!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

# Chamada da função principal
if __name__ == "__main__":
    main()