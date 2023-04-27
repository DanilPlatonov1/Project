# Задание 1
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 5 == 0:
#         print('Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     else:
#         print(i)

# Задание 2
# a = [1, 4, 6]
# b = [11, 33, 22]
# lst = list(zip(a, b))
# lst.sort(key=lambda x: x[1])
# print(a := [i for i, j in lst])
# print(b)

# Задание 4
# rim_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# def rim2int(rim_num):
#     summa = 0
#     for i, j in zip(rim_num, rim_num[1:]):
#         if rim_dic[i] < rim_dic[j]:
#             summa -= rim_dic[i]
#         else:
#             summa += rim_dic[i]
#     summa += rim_dic[rim_num[-1]]
#     return summa
# print(rim2int('MMXXIII'))
# print(rim2int('MVM'))
# print(rim2int('XM'))
# print(rim2int('XXXVX'))
# print(rim2int('CIX'))




