import random

# in case you want the user to be able to enter his/her own text
# test = input()

text = "The mind's ability to decipher a mis-spelled word if the first and last letters of the word are correct."

def typoglycemia(text):
    words = text.split()
    result = []
    for word in words:
        if len(word) > 3:
            substring = list(word[1:-1])
            random.shuffle(substring)
            substring = ''.join(substring)
            substring = word[0] + substring + word[-1]
            result.append(substring)
        else:
            result.append(word)
    return ' '.join(result)

print typoglycemia(text)
