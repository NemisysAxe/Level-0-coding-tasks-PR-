#task_0_5

#Defining the variables needed to calculate the area of a triangle.

def triangle_area(a, b, c):
    
    spm = (a + b + c) *0.5               #constant variable = 0.5
    
    a1 = spm - a
    b2 = spm - b
    c1 = spm - c
    spm2 = spm * (a1 * b2 * c1)
    
    tri_area = spm2 ** 0.5
    
    print(tri_area)
  

triangle_area(3, 4, 5)




