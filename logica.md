## Lógica de Programação com Python e Exercícios

Bem-vindo ao tutorial detalhado de lógica de programação com Python! Neste tutorial, vamos mergulhar fundo nos conceitos fundamentais da lógica de programação, abordar tipos de dados com mais detalhes e fornecer uma variedade de exercícios para você praticar. Vamos começar!

### 1. Introdução à Lógica de Programação

A lógica de programação é a capacidade de dividir um problema complexo em passos lógicos e sequenciais que um computador pode executar. Isso envolve a compreensão de conceitos como instruções sequenciais, estruturas de controle e funções.

#### 1.1 Instruções Sequenciais

Um programa consiste em instruções executadas em ordem sequencial. Cada instrução é um comando que o computador executa.

Exemplo em Python:
```python
print("Olá, mundo!")
print("Bem-vindo ao tutorial de lógica de programação.")
```

#### 1.2 Variáveis e Tipos de Dados

Python possui diversos tipos de dados que armazenam informações:

- **int**: Números inteiros (por exemplo: 5, -3, 100)
- **float**: Números de ponto flutuante (por exemplo: 3.14, -0.5, 1.0)
- **str**: Sequências de caracteres (por exemplo: "Olá", 'Python', "123")
- **bool**: Valores booleanos (True ou False)

Exemplo em Python:
```python
idade = 25  # int
altura = 1.75  # float
nome = "João"  # str
ativo = True  # bool
```

### 2. Estruturas de Controle

As estruturas de controle permitem que você tome decisões e repita ações.

#### 2.1 Condicionais (if, else, elif)

As estruturas condicionais executam diferentes blocos de código com base em condições.

Exemplo em Python:
```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

#### 2.2 Loops (for, while)

Os loops permitem que você execute um bloco de código repetidamente.

Exemplo de loop for em Python:
```python
for i in range(5):
    print(i)
```

Exemplo de loop while em Python:
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### 3. Funções

As funções são blocos de código reutilizáveis que podem ser chamados várias vezes.

Exemplo em Python:
```python
def saudacao(nome):
    print("Olá,", nome, "!")
    
saudacao("Maria")
saudacao("João")
```

### 4. Listas e Estruturas de Dados

As listas permitem armazenar múltiplos valores em uma única variável.

Exemplo em Python:
```python
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    print(num)
```

### 5. Exercícios - Tipos de Dados

Agora, pratique com exercícios relacionados aos tipos de dados:

1. Escreva um programa que calcule a área de um retângulo, dado a base e a altura.
2. Crie uma função que determine se um número é positivo, negativo ou zero.
3. Implemente um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa, usando peso e altura.

### 6. Exercícios - Estruturas de Controle

Agora, pratique com exercícios relacionados a estruturas de controle:

1. Escreva um programa que exiba os números pares de 1 a 20.
2. Crie um programa que solicite três números ao usuário e exiba o maior deles.
3. Implemente um jogo de adivinhação, onde o jogador tenta adivinhar um número entre 1 e 100.

### 7. Recursos Adicionais

Lembre-se de que este tutorial é uma base sólida. Python oferece muitos recursos avançados, como dicionários, conjuntos, manipulação de arquivos e bibliotecas externas.

### Conclusão

Parabéns por completar este tutorial detalhado! Você agora tem um entendimento profundo da lógica de programação com Python. Continue praticando, resolvendo problemas e explorando novos conceitos para aprimorar suas habilidades. À medida que avança, você estará preparado para enfrentar desafios mais complexos na programação. Bom trabalho!
