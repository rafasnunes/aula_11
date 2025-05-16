# Aula 11 - Exemplo de um Caixa Eletrônico

print('==== CAIXA ELETRÔNICO V 1.0 ====')

while True:
    try:

        saldo = 1000
        saque = float(input('Informe o valor para o saque: '))

    except ValueError as e:
        print(f'Erro: Digite apenas números. {e}')

    else:
        if saque > 0:
            if saldo >= saque:
                saldo -= saque
                print(f'O saque de R$ {saque} foi concluído.')
                break

            elif saque > saldo:
                print('Saldo insuficiente.')
        else:
            print('O saque precisa ser maior que R$ 0')


    finally:
        print(f'Seu saldo atual é: R$ {saldo}')