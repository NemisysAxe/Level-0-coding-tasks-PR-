#task_0_10

#This function returns the vowels from two string input.

def print_common_letters (string1, string2):
                          
    strings = string1 + string2
    
    vowels_upper = "AEIOU"
    vowels_lower = "aeiou"
    vowels = vowels_upper + vowels_lower
             
    for word1 in string1 and string2:
        if word1 in vowels and string1 and string2:
            print(word1, end= ",")
    
    for word1 in string1 and string2:
        if word1 in string1 and string2:
            if word1 not in vowels:
                print(word1)
     
    
print_common_letters('house','computers')




