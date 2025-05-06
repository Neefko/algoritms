# def findSmallIndex(arr):
#     small = arr[0]
#     smallIndex = 0
#     for i in range(len(arr)):
#         if arr[i] < small:
#             small = arr[i]
#             smallIndex = i
#     return smallIndex

# def selectSort(arr): # Сортировка с выбором
#     newArr = []
#     copiedArr = list(arr) # иначе мы не сможем повторно использовать arr тк его поменяли
#     for i in range(len(copiedArr)):
#         smallIndex = findSmallIndex(copiedArr)
#         newArr.append(copiedArr.pop(smallIndex))
#     return newArr

# def binary_search(arr, n): # Бинарный поиск
#     low = 0 # индекс наименьшего значения
#     high = len(arr) - 1 # индекс наибольшего значения
#     while high >= low: # пока есть непроверенные элементы
#         mid = (high + low) // 2 # находим среднее
#         if arr[mid] == n: # если среднее равняется искомому
#             return mid # возвращаем индекс искомого
#         elif arr[mid] > n: # если среднее больше чем искомое, значит оно левее середины
#             high = mid - 1 # присваеваем наибольшему значению индекс среднего-1(-1 тк мы уже проверили среднее значение)
#         else: # иначе, если среднее меньше чем искомое, значит оно правее середины
#             low = mid + 1  # присваеваем наименьшему значению индекс среднего+1(+1 тк мы уже проверили среднее значение)
#     return "Элемента нету" # Если мы не нашли элемент, значит его в списке нет

# def fastSort(arr):
#     if len(arr) < 2: # Если 0 или 1 элемент в массиве, то он уже отсортирован
#         return arr
#     else:
#         support = arr[0] # Опираемся на 1 эелемент и относительно его сортируем
#         less = [i for i in arr[1:] if i <= support] # Меньшая часть
#         most = [i for i in arr[1:] if i > support] # Большая часть
#         return fastSort(less) + [support] + fastSort(most) # [support] - тк нельзя складывать строки с другими типами данных

# listik = [5342, 56, 967, 15, 9, 1, 8]
# print(fastSort(listik))
# print(binary_search(fastSort(listik), 56))

# Поиск в ширину
from collections import deque
graph = {}
graph["вы"] = ["Алиса", "Боб", "Клэрg"]

def search(name):
    search_queue = deque() # создание новой очереди
    search_queue += graph[name] # Добавление в очередь графа
    searched = set () # массив для уже проверенных людей
    while search_queue: # проходимся по очереди
        person = search_queue.popleft() # берём первый в очереди элемент(самый левый)
        if not person in searched: # если в уже проверенных людях нет этого человека,то
            if person[-1] == 'g': # если его имя оканчивается на m то выводим его (как пример пусть у продовца в конце будет g)
                print(f"{person} продавец")
                return True
            else:
                try: 
                    search_queue += graph[person] # добавляются его соседи в очередь
                    searched.add(person) # добавление этой персоны в список прочитанных
                except KeyError:
                    pass
search("вы")