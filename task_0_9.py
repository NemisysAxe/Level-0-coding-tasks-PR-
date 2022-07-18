def print_vowels (word):

    word = word.lower()    
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    
    list_a = []
    
    if "a" in word:
        count_a = +1
        if count_a >= 1:
            list_a.append("a")
                   
    if "e" in word:
        count_e = +1
        if count_e >= 1:
            list_a.append("e")
        
    if "i" in word:
        count_i = +1
        if count_i >= 1:
            list_a.append("i")
                    
    if "o" in word:
        count_o = +1
        if count_o >= 1:
            list_a.append("o")
                
    if "u" in word:
        count_u = +1
        if count_u >= 1:
            list_a.append("u")
            
    
    for vowel in word and list_a:
        if vowel in list_a:
            print(vowel,end=",")


print('Vowels:', end= " ")                
#print_vowels('umuzi')
print_vowels("August")




