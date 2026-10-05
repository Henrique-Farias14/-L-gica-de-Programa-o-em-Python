'''
O que é uma função:

Uma função é um bloco de código criado para realizar uma determinada tarefa
Ele permite organizar e reutilizar código

1. Criando uma função:
Utilizar a palavra def para uma função
'''

def saudacao():
    print("Olá, sejam bem-vindos!")

saudacao()


'''
2. Criando uma função com parâmetros

parâmetros permitem enviar informações para a função.
'''

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ana")
saudacao("Maria")
saudacao("Guilherme")

'''
3. Mais de um parâmentro
'''
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)
apresentar("Guilherme", 20)

'''
4. Somando valores
'''

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar(10, 20)
somar(90, 10)

'''
5. Retornado um valor
Return devolve um valor para o local onde a função foi chamada
'''
def somar(numero1, numero2):
    return numero1 + numero2

print(somar(10, 5))

'''
6. Função com condição
'''

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(20))

'''
7. Parâmetro com valor padrão
'''
def saudacao(nome = "Aluno"):
    print(f"Olá, {nome}!")

saudacao("João")
saudacao()

'''
8. Função utilizando lista
'''
def calcularMedia(notas):
    soma = 0
    for nota in notas:
        print(nota)
        soma += nota

    return soma / len(notas)

notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"Média: {media}")

'''
9. Funções para organizar um programa
'''
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n====== PRODUTO =======")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)