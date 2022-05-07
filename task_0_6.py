#task_0_6

#This function returns the highest of three vaules    
def maximum(*x):
    large_num = x[0]
    
    for values in x:
        if values > large_num:
            large_num = values
    
    return large_num

#maxi_2 = maximum(1,22,3,2)
maxi_2 = maximum(1,5,27,50)
print(maxi_2)



