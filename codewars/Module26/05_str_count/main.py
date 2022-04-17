import os
from typing import Iterable


def string_count(directory: str = os.path.abspath('.').split(os.path.sep)[0] + os.path.sep,
                 count: list = []) -> Iterable:
    for i_dire in os.listdir(directory):
        i_path = os.path.join(directory, i_dire)
        suffix = ('.git', '.idea')
        if i_path.endswith(suffix):
            continue
        if i_path.endswith('.py'):
            with open(i_path, 'r', encoding='utf-8') as i_file:
                i_str_count = 0
                for line in i_file:
                    if line[:-1] and not line.startswith('#'):
                        i_str_count += 1
                if i_str_count > 0:
                    count.append(i_str_count)
                    yield sum(count)
        elif os.path.isdir(i_path):
            yield from string_count(directory=i_path, count=count)
    return


my_directory = os.path.abspath(os.path.join('..', '..', '..', 'python_basic'))
m = string_count(my_directory)
while True:
    action = input('Далее: ')
    try:
        if not action:
            print(next(m))
        else:
            break
    except StopIteration:
        print('Конец итерации')
