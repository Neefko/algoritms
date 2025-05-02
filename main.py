# def summ(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + summ(arr[1:])
# print(summ([1,2,3,4,5])) # Упражнение 4.1

# def elements(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return 1
#     else:
#         return 1 + elements(arr[1:])
# print(elements([1,2,3,4,5,4,6])) # Упражнение 4.2

# def bigNumber(arr):
#     if arr == []:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     elif arr[0] > bigNumber(arr[1:]):
#         return arr[0]
#     else:
#         return bigNumber(arr[1:])
# print(bigNumber([9,2,3,7,100,4,6]))
