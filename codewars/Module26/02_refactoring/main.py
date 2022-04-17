from collections.abc import Iterable


def my_generator(f_list_1: list, f_list_2: list, result_to_find: int) -> Iterable:
    for x in f_list_1:
        for y in f_list_2:
            result = x * y
            yield x, y, result
            if result == result_to_find:
                print('Found!!!')
                return x, y, result


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

resolution = my_generator(list_1, list_2, to_find)
for i_element in resolution:
    print(
        'x = {}, y = {}, result = {}'.format(
            i_element[0],
            i_element[1],
            i_element[2]
        )
    )

