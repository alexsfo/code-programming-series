# Programar em Python #18 - Argumentos Padrão

'''
	Os argumentos padrão têm como objetivo usar o seu valor padrão quando o utilizador não envia nenhum valor para esse mesmo argumento
'''

def estadoDaPorta(estado = True):
	if estado:
		print('A porta está aberta!');
	else:
		print('A porta está fechada!');

estadoDaPorta(False);