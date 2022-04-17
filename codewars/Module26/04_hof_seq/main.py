from typing import Iterable


class QSequence:
    def __init__(self, s) -> None:
        self.sequence = s[:]

    def __next__(self) -> int:
        try:
            q_element = self.sequence[-self.sequence[-1]] + self.sequence[-self.sequence[-2]]
            self.sequence.append(q_element)
            return q_element
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> Iterable:
        return self


q = QSequence([1, 1])
n = 10
while n != 0:
    element = next(q)
    print(element)
    n -= 1
