def write_log(*args,
              time=None,
              action=None,
              result=None,
              file='calc-history.log.csv'):
    import csv
    error = None
    try:
        with open(file, 'a', newline='') as f: # ?
            writer = csv.writer(f, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE, skipinitialspace=True)
            writer.writerow([time])
            writer.writerow([action + ':', args, '=', str(result) + '\n'])
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.csv'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                writer = csv.writer(backup_file, delimiter=' ', escapechar=' ', quoting=csv.QUOTE_NONE, skipinitialspace=True)
                writer.writerow([time])
                writer.writerow([action + ':', args, '=', str(result) + '\n'])
        except PermissionError as e:
            error = e
    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')