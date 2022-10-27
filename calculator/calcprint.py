def print_results(time, *args, action=None, result=None):
    from prettytable import PrettyTable
    x = PrettyTable()
    args_str = ", ".join(map(lambda i: str(i), args))
    x.field_names = ["Date/Time", "Operands", "Action", "Result"]
    x.add_row([time, args_str, action, result])
    print(x)
