
def triangle_area(a, b, c):
    
    spm = (a + b + c) *0.5               #constant variable = 0.5
    
    a1 = spm - a
    b2 = spm - b
    c1 = spm - c
    spm2 = spm * (a1 * b2 * c1)
    
    tri_area = spm2 ** 0.5
    
    x = print(tri_area)
    
    return x
  

triangle_area(3, 4, 5)




