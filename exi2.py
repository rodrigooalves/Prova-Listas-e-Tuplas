# Iniciando listas vazias para os numeros pares e impares
numeros = []
numeros_pares = []
numeros_impar = []

# Solicite ao usuario que digite 10 valores

for _ in range(10):
    valor = int(input("Digite o número: "))
    numeros.append(valor)
    
# Separe os numeros pares e impares

for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impar.append(numero)
        

tupla_numeros_impares = tuple(numeros_impar)
# Somando os valores dessa lista

quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impar)
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impar)

# Imprimindo os resultados
print("Números pares:", numeros_pares)
print("Números ímpares:", tupla_numeros_impares)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
