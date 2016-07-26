# Programar em Python #20 - Argumentos Flexíveis

'''
	Os argumentos flexíveis têm como objetivo fazer com que não seja necessário definir todos os argumentos de uma função quando forem indefinidos
	Resumindo, os argumentos flexíveis não têm um tamanho definido
	É necessário colocar o símbolo '*' antes de um argumento flexível ser definido na função
'''

def imprimirArgumentos(*argumentos):
	for argumento in argumentos:
		print('Argumento:', argumento);

imprimirArgumentos(1, 1.5, 'Eu sou uma string!', True, ['ABC', 'DEF', 'GHI']);