    
def maximum_value(*x):
    large_num = x[0]
    
    for values in x:
        if values > large_num:
            large_num = values
    
    return large_num

maxi_value = maximum_value(1,5,27,50)
print(maxi_value)



