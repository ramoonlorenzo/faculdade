# Operadores com números

Operações básicas com **números inteiros (int)** e **números de ponto flutuante (float)**.

## Sem biblioteca

### Soma

```python
a = 10 # int
b = 3.5 # float
soma = a + b
print(f"Soma: {a} + {b} = {soma}") # 13.5
```

### Subtração

```python
a = 10 # int
b = 3.5 # float
subtracao = a - b
print(f"Subtração: {a} - {b} = {subtracao}") # 6.5
```

### Multiplicação

```python
a = 10 # int
b = 3.5 # float
multiplicacao = a * b
print(f"Multiplicação: {a} * {b} = {multiplicacao}") # 35.0
```

### Divisão

```python
a = 10 # int
b = 3.5 # float
divisao = a / b
print(f"Divisão: {a} / {b} = {divisao}") # 2.857142857142857
```

### Divisão inteira (retorna o quociente da divisão, descartando o resto)

```python
a = 10 # int
b = 3.5 # float
divisao_inteira = a // b
print(f"Divisão inteira: {a} // {b} = {divisao_inteira}") # 2.0
```

### Resto da divisão (módulo)

```python
a = 10 # int
b = 3.5 # float
resto = a % b
print(f"Resto da divisão: {a} % {b} = {resto}") # 3.0
```

### Potenciação

```python
a = 10 # int
potencia = a ** 2
print(f"Potenciação: {a} ** 2 = {potencia}") # 100
```

## Com biblioteca (Math)

### Raiz quadrada

```python
a = 10 # int
raiz_quadrada = math.sqrt(a)
print(f"Raiz quadrada de {a} = {raiz_quadrada}") # 3.1622776601683795
```

### Logaritmo natural (base e)

```python
a = 10 # int
logaritmo_natural = math.log(a)
print(f"Logaritmo natural de {a} = {logaritmo_natural}") # 2.302585092994046
```

### Logaritmo na base 10

```python
a = 10 # int
logaritmo_base10 = math.log10(a)
print(f"Logaritmo na base 10 de {a} = {logaritmo_base10}") # 1.0
```

### Seno, Cosseno e Tangente (ângulo em radianos)

```python
angulo_radianos = math.radians(45) # Converte 45 graus para radianos
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f"Seno de 45 graus: {seno}") # 0.7071067811865475
print(f"Cosseno de 45 graus: {cosseno}") # 0.7071067811865476
print(f"Tangente de 45 graus: {tangente}") # 0.9999999999999999
```

### Arredondamento

```python
numero_float = 3.14159
arredondado = round(numero_float, 2) # Arredonda para 2 casas decimais
print(f"Arredondamento de {numero_float} para 2 casas decimais: {arredondado}") # 3.14
```

### Valor absoluto

```python
valor_negativo = -10
absoluto = abs(valor_negativo)
print(f"Valor absoluto de {valor_negativo} = {absoluto}") # 10
```

### Fatorial

```python
fatorial = math.factorial(5)
print(f"Fatorial de 5 = {fatorial}") # 120
```

### Constantes matemáticas

```python
print(f"Valor de pi: {math.pi}") # 3.141592653589793
print(f"Valor de e: {math.e}") # 2.718281828459045
```

---

# Operações com Strings

O que é uma string? Uma string é uma **sequência de caracteres, como palavras, frases ou textos**. Em Python, strings são definidas usando **aspas simples ('')** ou **aspas duplas ("")**.

## Básico

### Criação de Strings

```python
nome = "Alice"
sobrenome = 'Silva'
frase = "Python é incrível!"
```

### Exibindo Strings

```python
print("Nome:", nome) # Nome: Alice
print("Sobrenome:", sobrenome) # Sobrenome: Silva
print("Frase:", frase) # Frase: Python é incrível!
```

### Concatenação de Strings

"Concatenação" é a junção de duas ou mais strings.

```python
nome = "Alice"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print("Nome completo:", nome_completo) # Nome completo: Alice Silva
```

### Repetição de Strings

Você pode repetir uma string usando o operador de multiplicação.

```python
risada = "HA"
risada_repetida = risada * 3
print("Risada repetida:", risada_repetida) # Risada repetida: HAHAHA
```

### Acessando Caracteres de uma String

Em Python, strings são indexadas, o que significa que você pode acessar caracteres individuais usando índices.

```python
nome = "Alice"
primeiro_caractere = nome[0]
ultimo_caractere = nome[-1]
print("Primeiro caractere de 'Alice':", primeiro_caractere) # Primeiro caractere de 'Alice': A
print("Último caractere de 'Alice':", ultimo_caractere) # Último caractere de 'Alice': e
```

### Fatiamento de Strings (Slicing)

Você pode extrair partes de uma string usando o fatiamento.

```python
frase = "Python é incrível!"
parte_da_frase = frase[0:6] # Extrai os caracteres do índice 0 ao 5
print("Parte da frase:", parte_da_frase) # Parte da frase: Python
```

### Comprimento de uma String

Use a função **len()** para obter o número de caracteres em uma string.

```python
nome = "Alice"
tamanho_nome = len(nome)
print("Tamanho do nome 'Alice':", tamanho_nome) # Tamanho do nome 'Alice': 5
```

## Métodos de Strings

Strings em Python têm vários métodos úteis para manipulação.

### 1. lower() e upper(): Convertem a string para minúsculas ou maiúsculas.

```python
nome = "Alice"
minusculas = nome.lower()
maiusculas = nome.upper()
print("Nome em minúsculas:", minusculas) # Nome em minúsculas: alice
print("Nome em maiúsculas:", maiusculas) # Nome em maiúsculas: ALICE
```

### 2. strip(): Remove espaços em branco no início e no final da string.

```python
texto_com_espacos = " Olá, mundo! "
texto_sem_espacos = texto_com_espacos.strip()
print("Texto sem espaços:", texto_sem_espacos) # Texto sem espaços: Olá, mundo!
```

### 3. replace(): Substitui uma parte da string por outra.

```python
frase = "Python é incrível!"
nova_frase = frase.replace("incrível", "fantástico")
print("Frase modificada:", nova_frase) # Frase modificada: Python é fantástico!
```

### 4. split(): Divide a string em uma lista de substrings com base em um separador.

```python
frase = "Python é incrível!"
palavras = frase.split(" ")
print("Palavras da frase:", palavras) # Palavras da frase: ['Python', 'é', 'incrível!']
```

### 5. join(): Junta elementos de uma lista em uma única string, usando um separador.

```python
palavras = ["Python", "é", "incrível!"]
frase_reunida = " ".join(palavras)
print("Frase reunida:", frase_reunida) # Frase reunida: Python é incrível!
```

### 6. find(): Procura por uma substring e retorna o índice da primeira ocorrência.

```python
frase = "Python é incrível!"
indice = frase.find("incrível")
print("Índice de 'incrível':", indice) # Índice de 'incrível': 9
```

### 7. count(): Conta quantas vezes uma substring aparece na string.

```python
frase = "Python é incrível!"
contagem = frase.count("é")
print("Quantidade de 'é' na frase:", contagem) # Quantidade de 'é' na frase: 1F
```

### 8. startswith() e endswith(): Verificam se a string começa ou termina com uma substring.

```python
frase = "Python é incrível!"
comeca_com_python = frase.startswith("Python")
termina_com_incrivel = frase.endswith("incrível!")
print("Começa com 'Python'?", comeca_com_python) # Começa com 'Python'? True
print("Termina com 'incrível!'?", termina_com_incrivel) # Termina com 'incrível!'? True
```

## Formatação de Strings

Python oferece várias maneiras de formatar strings.

### 1. Usando f-strings (recomendado a partir do Python 3.6)

```python
nome = "Alice"
idade = 25
mensagem = f"{nome} tem {idade} anos."
print(mensagem) # Alice tem 25 anos.
```

### 2. Usando o método format()

```python
nome = "Alice"
idade = 25
mensagem = "{} tem {} anos.".format(nome, idade)
print(mensagem) # Alice tem 25 anos.
```

### 3. Usando o operador % (estilo antigo)

```python
nome = "Alice"
idade = 25
mensagem = "%s tem %d anos." % (nome, idade)
print(mensagem) # Alice tem 25 anos.
```

## Strings Multilinha

Você pode criar strings que ocupam várias linhas usando três aspas (simples ou duplas).

```python
poema = """Rosas são vermelhas,
Violetas são azuis,
Python é incrível,
E você também!"""
print("Poema:\n", poema)

"""Poema:
 Rosas são vermelhas,
Violetas são azuis,
Python é incrível,
E você também!"""
```

## Verificação de Caracteres

Você pode verificar se uma string contém apenas letras, números, etc.

```python
nome = "Alice"
print("'Alice' é alfabético?", nome.isalpha()) # 'Alice' é alfabético? True
print("'123' é numérico?", "123".isnumeric()) # '123' é numérico? True
print("'Python3' é alfanumérico?", "Python3".isalnum()) # 'Python3' é alfanumérico? True
```

---
