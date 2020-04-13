from random import randrange

score = 0
odpoved = 'ano'

while (odpoved !='ne') and (score <= 21):
    score = score + randrange(21)
    print('Tve score', score)
    if score <= 21: 
        odpoved = input('Pokracovat?')

if score > 21 :
    print('Prohral jsi')

if score == 21:
    print('Vyhral jsi')
