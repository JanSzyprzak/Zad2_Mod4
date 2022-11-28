

def palindrom(word):
    """ 
        Checks if word is a palindrom,
        Arguments:
        word     
    """
    my_list = []
    for i in range(len(word)):              
        if word[i].isalpha() == True or word[i].isnumeric() == True:
            my_list.append(word[i].upper())     
    if my_list == my_list[::-1]:  
        return True 
    else:
        return False          
    
print(palindrom("Ile Roman ładny dyndał na moreli"))
