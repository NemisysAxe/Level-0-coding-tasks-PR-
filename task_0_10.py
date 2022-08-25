def print_common_letters (string_a, string_b):
    
    string1 = string_a.lower()
    string2 = string_b.lower()
    
    output = " "
    
    for char in string1 and string2:
        if char in string1 and string2 and char not in output:
             output += char
             output += ","

    clean_list = output[:-1]     

    phrase = "Common letters"   
    print(f"{phrase}:{clean_list} ", end ='')


#print_common_letters("house","computers")
print_common_letters("baseball","basketball")
#print_common_letters("corporate", "cooperate")
#print_common_letters("muse", "music")
