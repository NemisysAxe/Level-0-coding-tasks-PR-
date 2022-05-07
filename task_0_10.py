#task_0_10

#This function returns the vowels from two string input.

def prcommon (string1, string2):
 #   solution1 = [word2 for word2 in string1 if word2 in string2]
  #  print(solution1)             
             
#string1 = str(" ")
#string2 = str(" ")
    strings = string1 + string2
    
    vowels_upper = "AEIOU"
    vowels_lower = "aeiou"
    vowels = vowels_upper + vowels_lower

    for word1 in strings:
        if word1 in vowels:
            print(word1, end=" ,")         
   
    print(word1, end=", ")
           # else:
            #    print(word2, end=", ")
            
prcommon('house','computers')




