import importlib


# noinspection SpellCheckingInspection
def main():
    print('2.9 Работа со словарями на языке Python.')

    task_number = int(input('\nВыберите номер задания: '))
    if 1 <= task_number <= 9:
        task_module = importlib.import_module(f'app.lab.lab_6.task_{task_number}')
        task_module.main()
    else:
        print('invalid input')


if __name__ == '__main__':
    main()
