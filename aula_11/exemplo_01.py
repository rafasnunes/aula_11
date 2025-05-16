# while True: - Repete a execução do programa até que as duas entradas de variáveis sejam atendidas.

tentativas = 3

while tentativas > 0:

    try:

        n1 = float(input('Número: '))
        n2 = float(input('Número: '))
        div = n1 / n2

        print(div)

        break

    except ZeroDivisionError:
        print('Erro: Não pode dividir por 0')

    except ValueError as e: # Variavel e recebe o código do erro
        print(f'Erro: Digite apenas números. - {e}')

    finally:
        print('App finalizado. Obrigado por utilizar nosso programa.')

    tentativas -= 1
    print(f'Número de tentativas {tentativas}')
