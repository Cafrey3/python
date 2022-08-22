# # 1
# # str = 'as 23 fdfdg544'
# # print(','.join(i for i in str if i.isdigit()))
#
# # 2
# # str = 'as 23 fdfdg544 34'
# # print(','.join(''.join(i if i.isdigit() else ' ' for i in str).split()))
#
# # 3
# # greeting = 'Hello, world'
# # print(list((greeting).upper()))
#
# # 4
# # print([i **2 for i in range(50) if i!=0])
#
# # 5
#
# # 5.1
# # def func(l):
# # for i in l:
# #     print(i)
# # func([1,2,3])
#
# # 5.2
# # def func(one,two,three):
# #     res= max(one,two,three)
# #     print(res)
# #     return res
# # func(1,2,3)
#
# # 5.3
# # def func(*args):
# #     print(max(*args))
# #     return min(*args)
# # func(1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99)
#
# # 5.4
# # def func(l):
# # print(max(l))
# # return max(l)
# # func([1, 2, 3, 4, 5])
#
# # 5.5
# # def func(l):
# #     print(min(l))
# #     return min(l)
# # func([1, 2, 3, 4, 5])
#
# # 5.6
# # def func(l):
# # res=0
# # for i in l:
# #     res+=i
# #     print(res)
# # return res
#
# # print(sum(l))
# # return sum(l)
# # func([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# # 5.7
# # def func(l):
# #     print(sum(l) / len(l))
# #     return sum(l) / len(l)
# # func([1, 2, 3, 4, 5, 6, 7, 8, 9])
#
#
# # 6
# l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
# def minimum():
#     print(min(l))
#
#
# minimum()
#
#
# def duplicate():
#     print(list(set(l)))
#
#
# duplicate()
#
#
# def x():
#     print(['x' if not (i + 1) % 4 else v for i, v in enumerate(l)])
#
#
# x()
#
#
# def square(n):
#     for i in range(n):
#         if i == 0 or i == n - 1:
#             print('*' * n)
#         else:
#             print('*' + ' ' * (n - 2) + '*')
#
#
# square(10)
#
#
# def table():
#     i = 1
#     while i <= 9:
#         a = 1
#         while a <= 9:
#             res = a * i
#             print(f'{res:3}', end='')
#             a += 1
#         i += 1
#
#
# table()
#
# while True:
#     print('1) minimum')
#     print('2) duplicate')
#     print('3) x')
#     print('4) square')
#     print('5) table')
#     print('0) exit')
#
#     type = input('Type: ')
#
#     if type == '1':
#         minimum()
#     elif type == '2':
#         duplicate()
#     elif type == '3':
#         x()
#     elif type == '4':
#         square(10)
#     elif type == '5':
#         table()
#     elif type == '0':
#         break
