#1. Estruturas Condicionais

nota = 6

if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')

# 2. Condições com operadores lógicos
#and --> todas as condições devem ser verdadeiras
#or --> pelo menos uma condição deve ser verdadeira
#not --> inverte o valor

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print('Entrada permitida')
else:
    print('Entrada negada.')

# 3. Estrutura de Repetição

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

# 4. Estrutura de repetição for
for numero in range(1, 6):
    print(numero)

# 5. Percorrendo uma lista

nomes = ['Ana', 'Carlos', 'João', 'Maria']

for nome in nomes:
    print(nome)

# 6. Break
# Break interrompre completamente a repetição
# Pass não executa nenhuma ação
for numero in range(1, 11):
    if numero == 7
        #break
        #pass
        continue
        print(numero)

# 7. Condição dentro de repetição
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} é Par")
    else:
        print(f"{numero} é Impar")