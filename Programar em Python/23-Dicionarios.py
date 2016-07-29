# Programar em Python #23 - Dicionários

'''
	Os dicionários são estruturas de dados que implementam mapeamentos (coleção de associações entre pares de valores)
	O primeiro elemento do par é chamado de chave (identificador) e o outro é chamado de conteúdo
'''

idades = {'Nelson Silva': 21, 'Maria Celeste': 37, 'Pedro Henrique': 52, 'Raquel Soares': 68};

idades['Pedro Henrique'] = 100;
del idades['Maria Celeste'];
idades.clear();

print(idades.items());
print(idades.keys());
print(idades.values());