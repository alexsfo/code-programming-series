# Programar em Python #16 - return

'''
	O return tem como objetivo retornar algo de uma função para que ao se chamar essa mesma se tenha acesso ao valor retornado
'''

def adicao():
	resultado = 0;

	for numero in range(1, 11):
		resultado += numero;

	return resultado;

print('Resultado da adição:', adicao());