import importlib

def main():
    lab_number = int(input('select lab number: '))
    if 1 <= lab_number <= 9:
        lab_module = importlib.import_module(f'app.lab.lab_{lab_number}.main')
        lab_module.main()
    else:
        print('invalid input')