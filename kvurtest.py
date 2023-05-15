import math

baddata = True
while baddata == True:
    try:
        a = int(input('Введите a:'))

        b = int(input('Введите b:'))

        c = int(input('Введите c:'))
        baddata = False
    except:

         print('Не удалось получить данные!')

D = ( b * b) - ( 4 * a * c )

if D > 0:
      print('Два корня')
      d = math.sqrt(D)
      x1 = ((-b) + d)/ (2 * a)
      x2 = ((-b) - d)/ (2 * a)

      print(f'Уравнение имеет два корня X1 = {x1}, X2 = {x2}.')

elif D == 0:
      print('Один корень')
      x = (-b)/ (2 * a)
      print(f'Уравнение имеет два корня X1 = {X1}')

else:
      print('Уравнение не имеет корней')