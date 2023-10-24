peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print(imc)

magreza = imc < 18.5
normal = imc >= 18.5 and imc <= 24.9
sobrepeso = imc >= 25 and imc <= 29.9
obesidade_grau_1 = imc >= 30 and imc <= 34.9
obesidade_grau_2 = imc >= 35 and imc <= 39.9

if magreza:
    print('Magreza')

if normal:
    print('Peso normal')

if sobrepeso:
    print('Sobrepeso')

if obesidade_grau_1:
    print('Obesidade grau I')

if obesidade_grau_2:
    print('Obesidade grau II')