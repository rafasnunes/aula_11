# Aula 11 - Utilizando o except para tratar erros diversos que podem ocorrer no programa.

try:

        n1 = float(input('Número: '))
        n2 = float(input('Número: '))
        div = n1 / n2

except Exception as e:
    print(f'Erro: {e}')

else:
    print(f'O resultado é: {div}')

finally: # Mensagem de finalização do programa.
    print('Fim da operação.')