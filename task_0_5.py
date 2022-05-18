
def triangle_area(a, b, c):
    
    semiparameter = (a + b + c) *0.5               #constant variable = 0.5
    
    a1 = semiparameter - a
    b2 = semiparameter - b
    c1 = semiparameter - c
    y = semiparameter * (a1 * b2 * c1)
    
    triangle_area = y ** 0.5
    
    x = triangle_area
    
    return x
  

print(triangle_area(3, 4, 5))




