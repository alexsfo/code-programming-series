# Programar em Python #22 - Erros Comuns

'''
	NameError: name 'variavel' is not defined -> Quando a variável apresentada não estiver definida
	IndentationError: expected an indented block -> Quando a indentação não for feita corretamente
	SyntaxError: EOL while scanning string literal -> Quando uma string não for finalizada (fechada)
	SyntaxError: invalid syntax -> Quando uma função não for fechada corretamente e não só
'''

variavel = 'Eu sou uma string!';
print(variavel);

def funcao():
	print('Eu faço parte desta função!');

print('Eu também sou uma string!');

print('Somos todos uma string!');