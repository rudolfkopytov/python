S = 0  # это наша переменная-счетчик, в которой мы будем считать сумму чисел
n = 1  # текущее натуральное число, с которого начинаем складывать натуральные числа

# заводим цикл while, который будет работать пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n-1)
#Первым делом необходимо определить, какое условие будет проверять цикл на каждой итерации. Это может быть любое выражение, которое возвращает булево значение — True или False.

Например, в нашем цикле мы хотим увеличивать переменную i на единицу до тех пор, пока она не станет равной 10. То есть наше выражение выглядит следующим образом: while i < 10.

Cтоит помнить, что перед тем как использовать какую-то переменную в цикле (в нашем случае это переменная i), её необходимо объявить.

2
Теперь необходимо определить действия, которые мы будем совершать внутри цикла.

В нашем случае это увеличение переменной i на единицу.

3
Наконец оборачиваем данную конструкцию в код. Для этого используем шаблон для создания цикла:

i = 0  # объявляем переменную
while i < 10:  # записываем условное выражение в цикл
    i += 1  # записываем действия в тело цикла