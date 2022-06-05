# 1. Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах:
#   a. до минуты: <s> сек;
#   b. до часа: <m> мин <s> сек;
#   c. до суток: <h> час <m> мин <s> сек;
#   d. *в остальных случаях: <d> дн <h> час <m> мин <s> сек.

# while True:
#     duration = int(input("Введите время в секундах:  "))
#     if duration < 60:
#         print(f"{duration} сек.")
#     elif duration >= 60 and duration < 3600:
#         print(f"{duration // 60} мин. {duration % 60} сек.")
#     elif duration >= 3600 and duration < 86400:
#         print(f"{duration // 3600} час. {(duration % 3600) // 60} мин. {duration % 60} сек.")
#     elif duration >=86400:
#         print(f"{duration // 86400} дн. {(duration % 86400) // 3600} час. {(duration % 3600) // 60} "
#               f"мин. {duration % 60} сек.")

# 2. Создать список, состоящий из кубов нечетных чисел от 1 до 1000 (куб Х - третья степень
#   числа Х):
#     a.Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#       Например, число <19 ^ 3 = 6859> будем включать в сумму, так как 6+8+5+9=28 - делится
#       нацела на 7. Внимание: использовать только арифметические операции!
#     b.К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
#       списка, сумма цифр которых делится нацело на 7.
#     c.*Решить задачу под пунктом b, не создавая новый список.

# a)

# my_list = []    # список из кубов нечетных чисел с 1 до 1000
# my_list_2 = []  # список сумма цифр которых делится нацело на 7
# sum = 0         # сумма цифр числа из my_list
# sum_num = 0     # сумма чисел из my_list_2
#
# for el in range(1, 1000, 2):
#     my_list.append(el ** 3)
#
# for num in my_list:
#     sum = 0
#     # num_for_while = num                    # если использовать только арифметические операции
#     # while num_for_while != 0:
#     #     sum += num_for_while % 10
#     #     num_for_while = num_for_while // 10
#     for el in str(num):
#         sum += int(el)
#     if sum % 7 == 0:
#         my_list_2.append(num)
#         sum_num += num
#
# print(my_list)
# print(my_list_2)
# print(sum_num)

# b)

# my_list = []    # список из кубов нечетных чисел с 1 до 1000
# my_list_2 = []  # список сумма цифр которых делится нацело на 7
# sum = 0         # сумма цифр числа из my_list
# sum_num = 0     # сумма чисел из my_list_2
#
# for el in range(1, 1000, 2):
#     my_list.append(el ** 3)
#
# for num in my_list:
#     sum = 0
#     num += 17
#     for el in str(num):
#         sum += int(el)
#     if sum % 7 == 0:
#         my_list_2.append(num)
#         sum_num += num
#
# print(my_list)
# print(my_list_2)
# print(sum_num)

# c)

# my_list = []    # список из кубов нечетных чисел с 1 до 1000
# sum_num = 0     # сумма чисел, сумма цифр которых делится нацело на 7
#
# for el in range(1, 1000, 2):
#     my_list.append(el ** 3)
#
# for num in my_list:
#     sum = 0   # сумма цифр числа из my_list
#     num += 17
#     for el in str(num):
#         sum += int(el)
#     if sum % 7 == 0:
#         my_list_2.append(num)
#         sum_num += num
#
# print(my_list)
# print(sum_num)

# 3. Склонение слова
#   Реализовать склонение слова "процент" во фразе "N процентов". Вывести эту фразу на
#   экран отдельной строкой для каждого из чисел в интервале от 1 до 100.

# for num in range(1, 101):
#     if num <= 20:
#         if num == 1:
#             word = 'процент'
#         elif num <= 4:
#             word = 'процента'
#         else:
#             word = 'процентов'
#         print(f'{num} {word}')
#     if num > 20:
#         if str(num)[-1] == '1':
#             word = 'процент'
#         elif str(num)[-1] <= '4' and str(num)[-1] != '0':
#             word = 'процента'
#         else:
#             word = 'процентов'
#         print(f'{num} {word}')
