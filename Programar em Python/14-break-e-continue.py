# Programar em Python #14 - break e continue

'''
	O break faz com que o a vida do ciclo termine, ou seja, faz com que não se itere por mais nada
	O continue ignora todo o conteúdo da volta que está a seguir dele mesmo e passa automaticamente para a próxima iteração
'''

numero = 0;
animais = ['Cão', 'Gato', 'Galinha', 'Coelho', 'Leão'];

for animal in animais:
	print('Animal:', animal);

	if animal == 'Coelho':
		break;

while numero < 10:
	numero += 1;

	if numero == 5:
		continue;

	print('Número da volta:', numero);