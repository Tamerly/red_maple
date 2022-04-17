# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array
# where an uppercase letter is a person standing up.

def wave(people):
    lst = list(people)
    result = []
    for index, letter in enumerate(lst):
        if letter.isalpha():
            work_space = lst[:]
            work_space[index] = letter.upper()
            result.append(''.join(work_space))

    return result


print(wave("hello"))