dia = int(input('coloque um dia da semana: '))

# match é utilizado para lidar com múltiplas condições
match dia:
    case 1:
        print('domingo')
    case 2:
        print('segunda')
    case 3:
        print('terça')
    case 4:
        print('quarta')
    case 5:
        print('quinta')
    case 6:
        print('sexta')
    case 7:
        print('sábado')

    # o _: é usado caso não seje executado nenhum dos casos acima
    # pode ser colocado também uma outra variável para receber a variável dia, mas não tem necessidade
    case _:
        print('dia inválido')