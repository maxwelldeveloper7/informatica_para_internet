from views import escreve_menu
import os
import models

if __name__ == "__main__":
    while(True):
        escreve_menu()
        opcao = 0 # esta variavel armazenará as opções do usuário
        opcao = input('Escolha sua opção: ')
        if opcao == '1':
            models.soma()
        elif opcao == '2':
            models.subtrai()
        elif opcao == '3':
            models.multiplica()
        elif opcao == '4':
            models.divide()
        elif opcao == '5':
            print('Sair!')
            break
        else:
            print('Opção inválida!')
        input('pressione enter para continuar')
        os.system('clear')