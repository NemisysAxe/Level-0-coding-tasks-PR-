def print_vowels (string):

    string = string.lower()
    vowels = "AEIOUaeiou".lower()    
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    
    list_a = []
    
    if "a" in string:
        count_a = +1
        if count_a >= 1:
            list_a.append("a")
            #print('a', sep=", ", end=",")
            
    if "e" in string:
        count_e = +1
        if count_e >= 1:
            list_a.append("e")
            #print('e', sep=", ",end=",")
        
    if "i" in string:
        count_i = +1
        if count_i >= 1:
            list_a.append("i")
            #print('i', sep=", ",end=",")
                
    if "o" in string:
        count_o = +1
        if count_o >= 1:
            list_a.append("o")
            #print('o', sep=", ",end=",")
                
    if "u" in string:
        count_u = +1
        if count_u >= 1:
            list_a.append("u")
            #print('u', sep=", ",end=",")
       
    
    for vowel in string and list_a:
        if vowel in list_a:
            print(vowel,end=",")
                
#print_vowels('umuzi')

print_vowels("August")




