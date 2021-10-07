# The goal of this exercise is to convert a string to a new string where each character in the new string is "("
# if that character appears only once in the original string, or ")" if that character appears more than once
# in the original string. Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word: str):
    data = {}
    for i_letter in word.lower():
        if i_letter not in data:
            data[i_letter] = 1
        else:
            data[i_letter] += 1

    result = ''
    for j_letter in word.lower():
        if data[j_letter] > 1:
            result += ')'
        else:
            result += '('
    return result


print(duplicate_encode('rEcede'))
