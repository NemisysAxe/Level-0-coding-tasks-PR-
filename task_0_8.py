def time(t):
    hours = (t // 60) 
    minutes = (t % 60)
   
    if hours <= 0 or hours == 1:
        h = "hour" 
    else:
        h = "hours"
        
    if minutes <= 0 or minutes == 1:
        m = "minute"
    else:
        m = "minutes"
            
    print(f"{hours} {h}, {minutes} {m}")
    
time(64)
