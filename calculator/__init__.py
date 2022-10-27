from .calclog import write_log
from .calcprint import print_results
from .main_module import load_params, PARAMS, convert_precision, f, calculate 
from datetime import datetime as dt


def calc():
    # 1. Ввод значений с клавиатуры
    # 2. Запуск calculate
    # 3. Вывод результатов вычислений
    load_params()
    ndigits = convert_precision(PARAMS['precision'])
    r_type = PARAMS['output_type']
    p_acts = PARAMS['possible_actions']
    dest = PARAMS['destination']
    act = input("Введите действие: ")
    if act not in p_acts:
        return print("Таких действий в калькуляторе нет")
    if act == 'S':
        ops_lst = []
        while True:
            op = (input("Введите аргумент: "))
            if op != "":
                ops_lst.append(float(op))
            else:
                break
        r = f(*ops_lst)
        r = round(r, ndigits)
        if r_type == int:
            r = int(r)
        current_time = str(dt.now())[0:19]
        print_results(current_time, *ops_lst, action=act, result=r)
        write_log(*ops_lst, time=current_time, action=act, result=r, file=dest)
    else:
        # использование try/except
        while True:
            try:
                op1 = float(input("Введите операнд 1: "))
                op2 = float(input("Введите операнд 2: "))
                break
            except ValueError:
                print("Операнды должны быть представлены в виде чисел!")
        r = calculate(op1, op2, act)
        r = round(r, ndigits)
        if r_type == int:
            r = int(r)
        current_time = str(dt.now())[0:19]
        print_results(current_time, *(op1, op2), action=act, result=r)
        write_log(*(op1, op2),
                  time=current_time,
                  action=act,
                  result=r,
                  file=dest)
