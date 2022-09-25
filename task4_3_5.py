import numpy as np

calculation = ''.join(input().split())
try:
    if 'e^' in calculation:  # e^(x + y) данные должны поступать в таком виде
        calculation = calculation.split('+')
        print(np.e ** (int(calculation[0][3:]) + int(calculation[-1][:len(calculation[-1]) - 1])))
    elif 'sin' in calculation:  # sin(x + y) данные должны поступать в таком виде
        calculation = calculation.split('+')
        print(np.sin(int(calculation[0][4:]) + int(calculation[-1][:len(calculation[-1]) - 1])))
    elif 'cos' in calculation:  # cos(x + y) данные должны поступать в таком виде
        calculation = calculation.split('+')
        print(np.cos(int(calculation[0][4:]) + int(calculation[-1][:len(calculation[-1]) - 1])))
    elif '^' in calculation:  # x^y данные должны поступать в таком виде
        calculation = calculation.split('^')
        print(np.power(int(calculation[0]), int(calculation[-1])))
    elif '+' in calculation:
        calculation = calculation.split('+')
        print(int(calculation[0]) + int(calculation[-1]))
    elif '-' in calculation:
        calculation = calculation.split('-')
        print(int(calculation[0]) - int(calculation[-1]))
    elif '∙' in calculation:
        calculation = calculation.split('∙')
        print(int(calculation[0]) * int(calculation[-1]))
    elif '÷' in calculation:
        calculation = calculation.split('÷')
        if calculation[-1] != '0':
            print(int(calculation[0]) // int(calculation[-1]))
        else:
            print('Division by zero')
    else:
        print('no valid operation found')
except:
    print('invalid input: see the examples')
