
def triangle_area(height, base, length):
    
    semiparameter = (height + base + length) *0.5               #constant variable = 0.5
    
    height1 = semiparameter - height
    base1 = semiparameter - base
    length1 = semiparameter - length
    y = semiparameter * (height1 * base1 * length1)
    
    x = y ** 0.5
    
    triangle_area = x
    
    return triangle_area
  

print(triangle_area(3, 4, 5))




