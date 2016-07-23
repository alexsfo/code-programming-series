# Programar em Python #17 - Argumentos

'''
	Os argumentos são como se fossem variáveis que recebem os seus valores (o seu conteúdo) quando a função é chamada
	Esses mesmos argumentos são considerados de variáveis locais porque só existem dentro da função
	As variáveis locais são descartadas quando se retorna ao ponto de chamada
'''

def dadosPessoais(nome, idade, nacionalidade):
	print('Nome:', nome);
	print('Idade:', idade);
	print('Nacionalidade:', nacionalidade);

dadosPessoais('Maria Celeste', 37, 'Inglesa');