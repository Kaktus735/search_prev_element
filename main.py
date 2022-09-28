import sys
import random


def qsort_random(array, left = 0, right = None):
    if right is None:  # Считаем, что правая граница не определена
        right = len(array) - 1

    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


# Модифицированный бинарный поиск
# Поиск возвращает позицию элемента, который равен или больше искомого
def binary_search(array, element, left = 0, right = None):
    if right is None:  # Считаем, что правая граница не определена
        right = len(array) - 1

    if left > right:  # если левая граница превысила правую,
        return left  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


def get_sequence():
    num_sequence = input('Введите последовательность чисел через пробел:\n')
    num_list = []
    count = 0
    for x_str in num_sequence.split():
        try:
            x_num = int(x_str)
        except ValueError:
            print('Ввод некорректен, проверьте, что ввод содержит последовательность чисел, разделенных пробелом')
            return
        num_list.append(x_num)
        count += 1
    if count < 2:
        print('Последовательность должна содержать минимум 2 цифры')
        return
    return num_list


def get_search_num():
    str_num_for_search = input('Введите искомое число:\n')
    try:
        num_for_search = int(str_num_for_search)
        return num_for_search
    except ValueError:
        print('Ввод некорректен, проверьте, что ввод содержит число')
        return


if __name__ == '__main__':
    print('Программа предназначена для поиска номера позиции элемента')
    print('Поиск происходит в списке чисел, получаемый из введенной пользователем последовательности чисел')
    print('Программа находит номер позиции элемента согласно условиям:')
    print('    - искомый элемент меньше введенного пользователем числа')
    print('    - элемент, следующий за искомым, больше или равен введенному пользователем числу\n')

    num_list = get_sequence()  # Получаем список последовательности чисел
    if num_list is None:
        sys.exit()
    num_for_search = get_search_num()  # Получаем введенное пользователем число
    if num_for_search is None:
        sys.exit()

    qsort_random(num_list)  # Сортируем список
    print('Отсортированный список: {}'.format(num_list))

    # Число в предыдущей позиции всегда будет меньше введенного пользователем числа
    search_position = binary_search(num_list, num_for_search)  # Ищем элемент в списке
    if search_position < len(num_list) and search_position > 0:
        print('Номер позиции искомого элемента {}, позиция считается от нуля'.format(search_position - 1))
    else:
        print('Номер позиции искомого элемента не был определен, условия поиска не были соблюдены')
