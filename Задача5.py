yesterdayTemp=float(input('Введите вчерашнюю температуру: '))
todayTemp=float(input('Введите сегодняшнюю температуру: '))
if todayTemp>yesterdayTemp:
    print('Сегодня теплее, чем вчера')
elif todayTemp<yesterdayTemp:
    print('Сегодня холоднее, чем вчера')
else:
    print('Температура одна')