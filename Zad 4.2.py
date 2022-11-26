

def palindrom(word):
    """ 
        Checks if word is a palindrom,
        Arguments:
        word     
    """
    for i in range(len(word)):       
        if word[i] == word[- i - 1] and i + 1 < len(word):           
            continue
        elif word[i] == word[- i - 1] and i + 1 == len(word):                    
            return True
        else:                      
            return False

print(palindrom("kajak"))
