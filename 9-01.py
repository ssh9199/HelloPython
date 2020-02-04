time = int(input('근무시간 : '))
salary = int(input('시급 : '))
money = 0

if time>12 :
    money += salary * 12
    money += int((salary * (time-12)) * 1.3)
else :
    money += salary * time

print('')
print('총 급여 : ', end='')
print(money, '원')
