#task_0_9

#This function returns the vowels from a single string value
def pvowels (string):

    vowels_upper = "AEIOU"
    vowels_lower = "aeiou"
    vowels = vowels_lower + vowels_upper
    
    for vowel in string:
        if vowel in vowels:
            if vowel > vowels_upper:  
                if vowel in vowels_lower:
                    print(vowel,end= ", ")
            
            #if vowel < vowels:
               # print(vowels,end= ", ")

                  
    
pvowels('Umuzi')




