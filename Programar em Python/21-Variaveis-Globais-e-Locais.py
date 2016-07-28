# Programar em Python #21 - Variáveis Globais e Locais

'''
	As variáveis globais são todas as que são definidas no exterior de uma função (na "raiz" do nosso código) e têm um alcance global
	As variáveis locais são todas as que são definidas no interior de uma função
	Resumindo, nem todas as variáveis são acessíveis a partir de todos os locais do nosso código
'''

acesso = 'Global';

def mudarAcesso():
	acesso = 'Local';
	print('Acesso no interior da função:', acesso);

mudarAcesso();
print('Acesso no exterior da função:', acesso);