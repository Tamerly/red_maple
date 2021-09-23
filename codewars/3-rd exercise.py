# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num: int) -> int:
    result = []
    for digit in str(num):
        result.append(str(int(digit) * int(digit)))
    return int(''.join(result))


print(square_digits(91))
