
def time(t):
    hours = (t // 60) 
    minutes = (t % 60)
    if hours == 1 and minutes == 1 :
        print((str(hours) + " hour") + ", " + ( str(minutes) + " minute") )
        
    if hours == 1 and minutes == 0 :
        print((str(hours) + " hour") + ", " + ( str(minutes) + " minutes") )
    
    if hours == 0 and minutes == 1 :
        print((str(minutes) + " minute"))
        
    if hours == 0 and minutes == 0 :
        print((str(hours) + " hours") + ", " + ( str(minutes) + " minutes") )    
    
    if hours == 1 and minutes > 1 :
        print((str(hours) + " hour") + ", " + ( str(minutes) + " minutes") )
    
    if hours <= 1 and minutes > 1 :
        print(( str(minutes) + " minutes"))
    
    if hours > 1 and minutes == 1 :
        print((str(hours) + " hours") + ", " + ( str(minutes) + " minute") )
    
    if hours > 1 and minutes > 1 :
        print((str(hours) + " hours") + ", " + ( str(minutes) + " minutes") )
        

    
time(60)



