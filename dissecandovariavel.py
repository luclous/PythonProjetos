print('Exercício dissecando uma variável')
a = input('Digite algo: ')
print('O tipo primitivo é:', type(a))
print('É um número?', a.isnumeric())
print('É uma letra?', a.isalpha())
print('Esta em maiusculo', a.isupper())
print('Esta em minusculo', a.islower())
print('É apenas espaços?', a.isspace())
print('É alfanumérico?', a.isalnum())
print('Esta captalizada?', a.istitle())
