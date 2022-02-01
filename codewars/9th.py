# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

def pig_it(text):
    work_space = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in work_space])
