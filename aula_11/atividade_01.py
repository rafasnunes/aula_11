# Criar um programa que peça duas notas ao usuário, calcule a média e informe
# se o = aluno foi aprovado. O programa deve:
# 1. Usar try para converter as notas para float.
# 2. Usar except para tratar erro caso o usuário digite texto/valor inválido.
# 3. Usar else (caso não dê erro no try) para: o Verificar se as notas estão
# no intervalo de 0 a 10.
# 4. Calcular e exibir a média.
# 5. Informar se o aluno foi aprovado (média ≥ 6).
# 6. Usar finally para exibir uma mensagem de encerramento do programa.

import os

try:

    print('\n ##### CALCULADOR DE MÉDIAS V 1.0 ##### \n \n')

    while True:

        try:

            n1 = float(input('Digite a primeira nota: '))
            n2 = float(input('Digite a segunda nota: '))

        except ValueError:
            os.system('cls')
            print('Digite apenas números.')

        else:
            if 0 <= n1 <= 10 and 0 <= n2 <= 10: # Ou poderia utilizar " if n1 in range(0, 10): "
                media = (n1 + n2) / 2
                print(f'A média do aluno é: {media}')

                if media >= 6:
                    print('Aluno aprovado!')
                    break
                else:
                    print('Aluno reprovado.')
                    break
            else:
                os.system('cls')
                print('As notas precisam estar no intervalo entre 0 e 10.')

finally:
    print('Obrigado por utilizar o programa.')