print('Добро пожаловать в калькулятор!')
print('1. Арифметические операторы (+, -, *, ...)')
print('2. Оперторы сравнения (>, <, >=, ...)')
print('3. Логические операторы (and, or, not)')
print('4. Операторы принадлежности (in, not in)')
print('5. Операторы тождественности (is, is not)')
print('0. Выход')
welc = float(input('Выберите действие: '))
print('-' * 45)

if welc == 1:
    print('Доступны следующие арифметические операторы: ')
    print('+; -; *; /; //; %; **')
    print('-' * 45)

    a = float(input('Введите первое число: '))
    oper = input('Введите оператор: ')
    b = float(input('Введите второе число: '))

    if oper == '+':
        print('Ваш результат: ', a + b)

    elif oper == '-':
            print('Ваш результат: ', a - b)

    elif oper == '*':
            print('Ваш результат: ', a * b)

    elif oper == '/' and b == 0:
            print('На ноль делить нельзя!')

    elif oper == '/':
        if b != 0:
              print('Ваш результат: ', round(a / b, 2))
        else: 
              print('На ноль делить нельзя')

    elif oper == '//':
            print('Ваш результат: ', a // b)

    elif oper == '%':
                print('Ваш результат: ',  a % b)

    elif oper == '**':
                print('Ваш результат: ', a ** b)

    elif oper == '':
        print('Вы забыли ввести оператор')

    else:
          print('Неопознанное действие')

elif welc == 2:
    print('Доступны следующие арифметические операторы: ')
    print('>; <; >=; <=; ==; !=')
    print('-' * 45)

    a = float(input('Введите первое число: '))
    oper = input('Введите оператор: ')
    b = float(input('Введите второе число: '))

    if oper == '>':
        if a > b:
            print(a > b)
        else:
            print('False')

    elif oper == '<':
        if a < b:
            print(a < b)
        else: 
            print('False')

    elif oper == '>=':
        if a >= b:
            print(a >= b)
        else: 
            print('False')

    elif oper == '<=':
        if a <= b:
            print(a <= b)
        else: 
            print('False')

    elif oper == '==':
        if a == b:
            print(a == b)
        else: 
            print('False')

    elif oper == '!=':
        if a != b:
            print(a != b)
        else: 
            print('False')

    elif oper == '':
        print('Вы забыли ввести оператор')
    
    else:
        print('Неопознанное действие')

elif welc == 3:
    print('Доступны следующие логические операторы: ')
    print('and; or; not (Инвертирует напрямую число при вводе)') 
    print('-' * 45)

    notA=input('Инвертировать первое число? (y/n): ')
    a = float(input('Введите первое число: '))

    oper = input('Введите оператор: ')

    notB=input('Инвертировать второе число? (y/n): ')
    b = float(input('Введите второе число: '))

    if oper == 'and':
        if notA or notB != '':
            if notA == 'y' and notB == 'y':
                    print(not(bool(a)) and not(bool(b)))
            elif notA == 'y' and notB == 'n':
                print(not(bool(a)) and bool(b))
            elif notA == 'n' and notB == 'y':
                print(bool(a) and not(bool(b)))
            elif notA == 'n' and notB == 'n':
                print(bool(a) and bool(b))
            else:
                print('Вы не ввели корректную инвертируемость')
        else:
            print('Вы не ввели инвертируемость')

    elif oper == 'or': 
        if notA or notB != '':
            if notA == 'y' and notB == 'y':
                print(not(bool(a)) or not(bool(b)))
            elif notA == 'y' and notB == 'n':
                print(not(bool(a)) or bool(b))
            elif notA == 'n' and notB == 'y':
                print(bool(a) or  not(bool(b)))
            elif notA == 'n' and notB == 'n':
                print(bool(a) or bool(b))
            else:
                print('Вы не ввели корректную инвертируемость')
        else:
            print('Вы ничего не ввели')

    elif oper == '':
        print('Вы забыли ввести оператор')

    else:
        print('Неопозднанное действиие')

elif welc == 4:
    print('Доступны следующие логические операторы: ')
    print('in; not in')
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('Такой список чисел мы имеем:', list)
    print('-' * 45)

    a = int(input('Введите число, принадлежность к списку которого мы должны проверить: '))
    oper = input('Введите оператор: ')

    if oper == 'in':
        print(a in list)

    elif oper == 'not in':
        print(a not in list)

    elif oper == '':
        print('Вы забыли ввести оператор')

    else:
        print('Неопозднанное')

elif welc == 5:
    print('Доступны следующие логические операторы: ')
    print('is; is not')
    print('-' * 45)
    
    a = float(input('Введите первое число: '))
    oper = input('Введите оператор: ')
    b = float(input('Введите второе число: '))

    prir = input('Прировнять первое число ко второму (y/n): ')

    if oper == 'is':
        if prir == 'y':
            a = b
            print(a is b)
        elif prir == 'n':
            print(a is b)

    elif oper == 'is not':
        if prir == 'y':
            a == b
            print(a is not b)
        elif prir == 'n':
            print(a is not b)

    elif oper == '':
        print('Вы забыли ввести оператор')
    
    else:
        print('Неопознанное действие')
    
elif welc == 0:
    print('Досвидания!')

elif not(0 <= welc <= 5) or welc // 10 == 0:
    print('Неопознанный оператор')