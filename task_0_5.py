
def triangle_area(height, base, length):
    
    semiparameter = (height + base + length) *0.5               #constant variable = 0.5
    
    height1 = semiparameter - height
    base1 = semiparameter - base
    length1 = semiparameter - length
    semiparameter_factor = semiparameter * (height1 * base1 * length1)
    
    x = semiparameter_factor ** 0.5
    
    tri_area = x
    
    return tri_area
  

print(triangle_area(3, 4, 5))




