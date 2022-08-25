def search_vowels(string):
    lowercase_string = string.lower()
    
    vowel = ['a','e','i','o','u']
    
    vowelist = " "
    
    for char in lowercase_string:
        if char in vowel:
            if char not in vowelist:
                vowelist += char
                vowelist += ","
                continue    
        else:
            if char in vowelist: 
                continue
        
        clean_list = vowelist[:-1]
                
    print(f"Vowels:{clean_list}" , end = " ")
      
search_vowels("August")



