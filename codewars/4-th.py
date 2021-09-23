# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_dict = dict([(i_letter, str(i_index + 1)) for i_index, i_letter in enumerate(alphabet)])
    result = []
    for j_letter in text.lower():
        if j_letter.isalpha():
            result.append(alphabet_dict[j_letter])

    return ' '.join(result)


print(alphabet_position("The sunset sets at twelve o' clock."))
