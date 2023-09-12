## Resolução dos Exercícios

**Exercício 1:**

```python
for i in range(1, 11):
    print(i)
```

**Exercício 2:**

```python
soma = 0
for i in range(1, 101):
    soma += i
print("A soma dos números de 1 a 100 é:", soma)
```

**Exercício 3:**

```python
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
```

**Exercício 4:**

```python
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
print(f"O fatorial de {numero} é {fatorial}.")
```

**Exercício 5:**

```python
n = int(input("Digite a quantidade de números na sequência de Fibonacci: "))
fibonacci = [0, 1]
for i in range(2, n):
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo)
print("Sequência de Fibonacci:", fibonacci)
```

**Exercício 6:**

```python
numero = int(input("Digite um número: "))
primo = True
if numero <= 1:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
if primo:
    print("O número é primo.")
else:
    print("O número não é primo.")
```

**Exercício 7:**

```python
frase = input("Digite uma frase: ").lower()
vogais = 'aeiou'
contagem = 0
for letra in frase:
    if letra in vogais:
        contagem += 1
print(f"A frase contém {contagem} vogais.")
```

**Exercício 8:**

```python
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
primos = []

for numero in range(inicio, fim + 1):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                break
        else:
            primos.append(numero)

print(f"Os números primos no intervalo de {inicio} a {fim} são: {primos}")
```

**Exercício 9:**

```python
decimal = int(input("Digite um número decimal: "))
binario = ""
while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print("O número em binário é:", binario)
```

**Exercício 10:**

```python
import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
```

Essas são as soluções para os exercícios propostos. Espero que isso ajude a aprimorar suas habilidades de programação em Python. Sinta-se à vontade para explorar e modificar as soluções para aprender mais.