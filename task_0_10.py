
def print_common_letters (string1, string2):
                          
    strings = string1 + string2
    
    vowels_uppercase = "AEIOU"
    vowels_lowercase = "aeiou"
    vowels = vowels_uppercase + vowels_lowercase
             
    for word1 in string1 and string2:
        if word1 in vowels and string1 and string2:
            print(word1, end= ",")
    
    for word1 in string1 and string2:
        if word1 in string1 and string2:
            if word1 not in vowels:
                print(word1, sep=",")
     
    
print_common_letters('house','computers')




