import random

imc = random.uniform(13.5, 35.0)

print(f'imc: {imc}')

if imc < 18.5:
    print('O imc é de, ' + str(imc) + ', que significa abaixo do peso')

elif imc < 25:
    print('O imc é de, ' + str(imc) + ', o que significa peso normal')

elif imc >= 25:
    print('O imc é de, ' + str(imc) + ', o que significa sobrepeso')

elif imc >= 30:
    print('O imc é de, ' + str(imc) + ', o que significa peso normal')