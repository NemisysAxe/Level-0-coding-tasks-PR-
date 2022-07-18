
def print_common_letters (char1, char2):
    
    cha1 = char1.lower()
    cha2 = char2.lower()
    
    for word1 in cha1 and cha2:
        if word1 in cha1 and cha2:
                print(word1, end = ",")
        
phrase = "Common letters"   
print(f"{phrase}: " , end ='') 
print_common_letters('house','computers')

