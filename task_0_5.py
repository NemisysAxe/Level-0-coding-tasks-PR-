def triangle_area(height, base, length):
    
    semiparameter = (height + base + length) *0.5                   
    semi_height = semiparameter - height
    semi_base = semiparameter - base
    semi_length = semiparameter - length
    semiparameter_factor = semiparameter * (semi_height * semi_base * semi_length)
    
    tri_area = semiparameter_factor ** 0.5
    
    return tri_area

print(triangle_area(3, 4, 5))




