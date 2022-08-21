def search_vowels(wordz):
    changed_word = wordz.lower()
    
    vowel = ['a','e','i','o','u']
    
    vowelist = " "
    
    for x in changed_word:
        if x in vowel:
            if x not in vowelist:
                vowelist += x
                vowelist += ","
                continue    
        else:
            if x in vowelist: 
                continue
        
        clean_list = vowelist[:-1]
                
    print(f"Vowels:{clean_list}" , end = " ")

if __name__ == "__main__":      
    search_vowels("August")



