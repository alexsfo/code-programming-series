# Programar em Python #25 - Funções Matemáticas

'''
	sin(variavel), cos(variavel) e tan(variavel) -> Calcular o seno, o cosseno e a tangente
	floor(variavel) -> Remove o valor decimal do dado número
	ceil(variavel) -> Arredonda o dado número para o próximo
	abs(variavel) -> Retorna o valor absoluto do dado número
	fsum(variavel) -> Faz a soma de todos os números dentro de uma lista (por exemplo)
	pow(variavel) -> Multiplica o seu valor inicial múltiplas vezes (consoante o número de vezes)
'''

from math import *;

numeros = [10, 20, 30, 40, 50];

print('Resultado da função sin():', sin(10.5));
print('Resultado da função cos():', cos(10.5));
print('Resultado da função tan():', tan(10.5));
print('Resultado da função floor():', floor(10.5));
print('Resultado da função ceil():', ceil(10.5));
print('Resultado da função abs():', abs(10.5));
print('Resultado da função fsum():', fsum(numeros));
print('Resultado da função pow():', pow(2, 5));