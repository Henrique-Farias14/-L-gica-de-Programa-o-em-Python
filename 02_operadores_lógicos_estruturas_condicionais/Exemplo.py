# Aula: OPERADORES LÓGICOS E ESTRUTURAS CONDICIONAIS
# 1. OPERADORES LÓGICOS

# and
# Todas as condições precisam ser verdadeiras

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)

# or
# Pelo menos uma das condições precisa ser verdadeira

idade = 16
acompanhado = True

resultado = idade >= 18 or acompanhado
print(resultado)

#not
# Inverte o resultado de uma condição

Aluno_matriculado = True

print(not Aluno_matriculado)

# 2. OPERADORES DE COMPARAÇÃO

idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

# 3. ESTRUTURA if / else

idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")