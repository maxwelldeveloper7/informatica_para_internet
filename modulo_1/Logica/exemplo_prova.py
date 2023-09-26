hora = 0
nome = ''
saudacao = ''

while(True):
    print('Este programa recebe o nome e hora do usuário, e faz uma Saudação!')
    print('')
    nome = input('Informe o seu nome: ')
    hora = input('Informe as horas: ')
    hora = int(hora) 
    if hora >= 0 and hora <= 5:
        saudacao = 'Boa madrugada'
    if hora >= 6 and hora <= 11:
        saudacao = 'Bom dia'
    if hora >= 12 and hora <= 17:
        saudacao = 'Boa tarde'
    if hora >= 18 and hora <= 23:
        saudacao = 'Boa noite'
    print('')
    print(f'{saudacao} {nome}!')
    print('')
    sair = input('Deseja sair do programa? (sim para sair)')
    if sair == 'sim':
        break

print('Fim do programa!')
    