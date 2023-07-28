p = str(input('Digite uma frase qualquer:')).lower().strip()
v = p.count('a')
q = p.find('a') +1

print(f'a letra a aparece {v} vezes' )
print(f'a primeira letra A apareceu na posição {q}')