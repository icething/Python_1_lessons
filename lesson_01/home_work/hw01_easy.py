
__author__ = 'Таланов Илья Дмитриевич'

# Задача-1: Запросите у пользователя ввод произвольного целого числа
# Необходимо вывести поочередно цифры введенного пользователем числа

chislo = input('Введите произвольное число ')
for i in chislo:
	print(i)

# Задача-2: Запросите у пользователя ввод двух чисел и связать значения с соответствующими переменными
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input('Введите первое значение ')
b = input('Введите второе значение ')
print(b, a)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите ваш возраст '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')


