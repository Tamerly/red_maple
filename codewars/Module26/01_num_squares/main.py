from collections.abc import Iterable


class MyIterator:
    def __init__(self, number: int) -> None:
        self.__limit = number
        self.__counter = 0

    def __next__(self) -> int:
        if self.__counter < self.__limit:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration

    def __iter__(self) -> Iterable:
        return self


def generator_function(number: int) -> Iterable:
    for i in range(1, number + 1):
        yield i ** 2


n = int(input('Enter digit: '))

first = MyIterator(number=n)
for i_element in first:
    print(i_element, end=' ')
print()

second = generator_function(number=n)
for j_element in second:
    print(j_element, end=' ')
print()

third = (k ** 2 for k in range(1, n + 1))
for k_element in third:
    print(k_element, end=' ')
print()


