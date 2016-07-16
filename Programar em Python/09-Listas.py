# Programar em Python #09 - Listas

'''
	Uma lista é um conjunto ordenado de valores, onde cada valor é identificado por um índice
	Os valores que compõem uma lista são chamados de elementos
'''

lista = ['Eu sou uma string!', 10, 10.5, True, ['A', 'B', 'C']];

lista[0] = 'Eu continuo a ser uma string na mesma!';

print('Fatiamento:', lista[:3]);

print('Conteúdo da lista:', lista);
print('Número de elementos da lista:', len(lista[4]));