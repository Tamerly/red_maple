# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers
# differs from the others. Bob observed that one number usually differs from the others in evenness.
# Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different
# in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test,
# which means indexes of the elements start from 1 (not 0)

def iq_test(numbers: str):
    data = numbers.split()
    odd = 0
    even = 0
    for element in data:
        if int(element) % 2 != 0:
            odd += 1
        else:
            even += 1

    if odd < even:
        for index, element in enumerate(data):
            if int(element) % 2 != 0:
                return index + 1
    else:
        for index, element in enumerate(data):
            if int(element) % 2 == 0:
                return index + 1


print(iq_test("2 4 7 8 10"))