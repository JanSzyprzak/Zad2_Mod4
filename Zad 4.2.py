

def palindrom(word):
    for i in range(len(word)):
        if word[i] == word[-1 - i]:
            return True
        else:
            return False



print(palindrom("test"))