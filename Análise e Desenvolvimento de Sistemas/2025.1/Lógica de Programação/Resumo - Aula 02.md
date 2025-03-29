# Operadores com números

Operações básicas com **números inteiros (int)** e **números de ponto flutuante (float)**.

**Exemplos:**

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
