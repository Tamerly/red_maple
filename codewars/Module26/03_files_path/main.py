import os
from collections.abc import Iterable


def gen_files_path(folder_to_find: str, root: str = os.path.abspath('.').split(os.path.sep)[0]+os.path.sep) -> Iterable:
    for i_dire in os.listdir(root):
        if i_dire == '.git':
            continue
        i_path = os.path.join(root, i_dire)
        if i_path.split(os.path.sep)[-1] == folder_to_find:
            yield ''.join(['Искомая директория ', i_path])
            return
        else:
            yield i_path
            if os.path.isdir(i_path):
                yield from gen_files_path(folder_to_find, i_path)


my_folder = '06_linked_list'
my_root = os.path.abspath(os.path.join('..', '..', '..', 'python_basic'))

for elem in gen_files_path(my_folder, my_root):
    print(elem)