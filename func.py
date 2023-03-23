from random import randint


def operation_math():
    """
    Funcao que retorna uma lista com os dados de um calculo aleatorio. Com seu resultado, tipo de operacao, primeiro
    valor e segundo valor.
    :return: Retorna uma lista com os dados do calculo
    """
    operations = randint(1, 4)
    number_one = randint(1, 100)
    number_two = randint(1, 100)

    if operations == 1:
        result = number_one + number_two
    elif operations == 2:
        result = number_one - number_two
    elif operations == 3:
        result = number_one * number_two
    else:
        if number_one % number_two == 0 and number_one != number_two:
            result = int(number_one / number_two)
        else:
            while True:
                number_one = randint(1, 100)
                if number_one % number_two == 0 and number_one != number_two:
                    result = int(number_one / number_two)
                    break

    return [operations, number_one, number_two, result]
