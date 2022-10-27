import math


PARAMS = {
    'precision': None,
    'output_type': None,
    'possible_actions': None,
    'destination': None
}


def load_params(file="params.ini"):
    import configparser
    global PARAMS
    config = configparser.ConfigParser()
    try:
        config.read(file)
        PARAMS['precision'] = config['Params']['precision']
        PARAMS['output_type'] = config['Params']['output_type']
        PARAMS['possible_actions'] = config['Params']['possible_actions']
        PARAMS['destination'] = config['Params']['destination']
    except PermissionError:
        PARAMS['precision'] = 0.001
        PARAMS['output_type'] = float
        PARAMS['possible_actions'] = [
            'S', '+', '-', '*', '/', '^', '//', '%%', '//%%'
        ]
        PARAMS['destination'] = 'calc-history.log.csv'


def convert_precision(precision):
    """
    Эта функция возвращает количество знаков дробной части от заданной точности

    precision: значение заданной точности

    >>> convert_precision("0.000001")
    6

    >>> convert_precision("0.001")
    3
    """
    i = 1
    while float(precision) * 10**i < 1:
        i += 1
    return i


def f(*args):
    """
    Эта функция возвращает среднеквадратическое отклонениние (S)

    *args: список произвольного количества числовых значений,
    необходимых для нахождения S

    >>> f(2,2,4,4)
    1.0

    >>> f(10,1,10,1)
    4.5
    """
    averagex = 0
    count = 0
    for n in args:
        averagex += n
        count += 1
    averagex /= count
    disper = 0
    for n in args:
        disper += (n - averagex)**2
    deviS = math.sqrt(disper / count)
    return deviS


def calculate(op1, op2, act):
    """
    Эта функция определяет, какое действие требуется выполнить, и возвращает
    соответствующее значение полученного выражения

    op1: значение первого операнда

    op2: значение второго операнда

    act: действие, необходимое выполнить с операндами

    >>> calculate(1,0,"/")
    'Деление на ноль невозможно'

    >>> calculate(15,-15,"*")
    -225
    """

    if act == '+':
        r = op1 + op2

    elif act == '-':
        r = op1 - op2

    elif act == '*':
        r = op1 * op2

    elif act == '/':
        if op2 != 0:
            r = op1 / op2
        else:
            r = 'Деление на ноль невозможно'

    elif act == "^":
        if op2 % 1 == 0:
            r = op1**op2

    elif act == '//':
        if op2 != 0:
            r = op1 // op2
        else:
            r = 'Деление на ноль невозможно'

    elif act == '%':
        if op2 != 0:
            r = op1 % op2
        else:
            r = 'Деление на ноль невозможно'

    elif act == '//%':
        if op2 != 0:
            r = divmod(op1, op2)
        else:
            r = 'Деление на ноль невозможно'
    else:
        print('Такой операции нет')

    return r