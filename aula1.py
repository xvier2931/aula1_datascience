# nome = "Ana"
# numero_inteiro = 10
# numero_real = 0.10
# dado_boleano = True

# print('texto')
# print(numero_inteiro)
# print(numero_real)
# print(dado_boleano)

# #mostrar

# print(type("texto"))
# print(type(numero_inteiro))
# print(type(numero_real))
# print(type(dado_boleano))

# text = type('texto')
# inteiro = type(numero_inteiro)
# real = type(numero_real)
# boleano = type(dado_boleano)

# print(f'Essa variável ->, {nome} ,é da, {text} ' )
# print(f'Essa variável->, {numero_inteiro}  ,é dá, {inteiro}' )
# print(f'Essa variável ->, {numero_real}   ,é dá, {real}' ) 
# print(f'Essa variável ->, {dado_boleano}  ,é dá, {boleano} ' )

# nome = 'Fernando'
# nome = 'Jr'
# print(nome)

# NOME = 'Caio' #não altere
# NOME = 'Karol'
# print(NOME)

# def nome():
#     name = 'Maria'
#     return name

# NOME = nome()
# print(NOME)

# print(10//12)

# # * / + -

# nome = input('Digite deu nome:')

# print(nome)

# numero1 = input('>>')
# numero2 = input('>>')

# calcular = numero1 + numero2
# print(calcular)


# x = 10
# text = str(x)
# n = text + 1 
# print(x)

numero1 = int(input('>>'))
numero2 = int(input('>>'))

soma = numero1 + numero2
divisão = numero1 / numero2
multiplicacao = numero1 * numero2
subritacao = numero1 - numero2 
print('soma', soma, divisão, 'divisão', multiplicacao, 'multiplicacao', subritacao, 'subritacao')


numero = 10

numero = [10,2,3,5, 'a',True,20]
print(numero)

numero[0] = 20
print(numero)

lista = [10,15,3,1,2]
indice = lista[0]
indice2 = lista[1]

print(indice + indice2)

numeros1 = list(range(1,11))
print(numero1)

# tuplas 
# listas imutáveis
# usamos parentenses 

tupla = (1,2,150,6,9)
tupla.append (22)
tupla[0] = 10
print(tupla {2})

tupla = (1,2,150,6,9,9,9,9)
print(tupla[2])
# conta a quantidade de valores 
# que foi declarado no parenteses
contador = tupla.count(9)

# verificra o indice do valor 
indice = tupla.index(9)
print(contador, indice)

# tamanho len()
print(len(tupla))

#max e min

maior = max(tupla)
menor = min(tupla)
print (menor , maior)

ordenar = sorted(tupla)
print(ordenar)

tupla4 = (1,4546,1,89,3,4,656)
sorted(tupla4)
a,b,c,d,e,f,g = tupla4
print(a,b,c,d,e,f,g)

# conjunto {}

nome = {1,5,150,56,89,78}
conjunto2 = {1,6,6}

diferenca = nome - conjunto2
nome.diferenca(conjunto2)
print(diferenca)
print(nome.diferenca(conjunto2))

conjunto4 = set([1,56,6])

dicionario={
'nome' : 'Pedro',
'idade'  : 25,
'endereco': 'Rua 100'
'curso': 'Python60h',

}
print(dicionario.values)













