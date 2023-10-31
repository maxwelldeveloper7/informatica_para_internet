import json
from datetime import datetime

# Função para registrar o ponto
def registrar_ponto():
    nome = input("Digite o seu nome: ")
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Tenta abrir o arquivo JSON existente ou cria um novo se não existir
    try:
        with open('registro_ponto.json', 'r') as arquivo:
            registros = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        registros = []

    # Adiciona o novo registro
    registros.append({'nome': nome, 'entrada': data_hora, 'saida': None})

    # Salva os registros de volta no arquivo JSON
    with open('registro_ponto.json', 'w') as arquivo:
        json.dump(registros, arquivo, indent=2)

    print(f'Entrada registrada para {nome} às {data_hora}')

# Função para calcular horas trabalhadas
def calcular_horas_trabalhadas(registro):
    if registro['entrada'] and registro['saida']:
        entrada = datetime.strptime(registro['entrada'], "%Y-%m-%d %H:%M:%S")
        saida = datetime.strptime(registro['saida'], "%Y-%m-%d %H:%M:%S")
        diferenca = saida - entrada
        return str(diferenca)

    return "Horas não calculadas"

# Função para exibir todos os registros
def exibir_registros():
    try:
        with open('registro_ponto.json', 'r') as arquivo:
            registros = json.load(arquivo)
            for registro in registros:
                print(f"Nome: {registro['nome']}, Entrada: {registro['entrada']}, Saída: {registro['saida']}, Horas Trabalhadas: {calcular_horas_trabalhadas(registro)}")
    except (FileNotFoundError, json.JSONDecodeError):
        print("Nenhum registro encontrado.")

# Menu principal
while True:
    print("\nMenu Principal:")
    print("1. Registrar Entrada")
    print("2. Registrar Saída")
    print("3. Exibir Registros")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        registrar_ponto()
    elif opcao == '2':
        nome = input("Digite o seu nome: ")
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open('registro_ponto.json', 'r') as arquivo:
                registros = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhum registro de entrada encontrado para o nome fornecido.")
            continue

        encontrado = False
        for registro in registros:
            if registro['nome'] == nome and registro['entrada'] and not registro['saida']:
                registro['saida'] = data_hora
                encontrado = True
                break

        if encontrado:
            with open('registro_ponto.json', 'w') as arquivo:
                json.dump(registros, arquivo, indent=2)
            print(f'Saída registrada para {nome} às {data_hora}')
        else:
            print("Registro de entrada não encontrado para o nome fornecido ou saída já registrada.")
    elif opcao == '3':
        exibir_registros()
    elif opcao == '4':
        print("Encerrando o aplicativo.")
        break
    else:
        print("Opção inválida. Tente novamente.")
