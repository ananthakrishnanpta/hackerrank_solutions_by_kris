def kangaroo(x1, v1, x2, v2):
    # Write your code here
    flag = 0
    if x1 < x2 and v1 <= v2 or x1 > x2 and v1 > v2:
        flag = 0
    else:
        if (x1 - x2) % (v1 - v2) == 0:
            flag = 1
            
    """
    displacement = initial_position + velocity * time
    
    x1 + (v1 * t) = x2 + (v2 * t)
    
    => (x1 - x2) = (v2 * t) - (v1 * t)
    => (x1 - x2) = (v2 - v1) * t
    => t = (x1 - x2) / (v2 - v1)
    
    for the kangaroos to meet at the common position at the same time, this t must be an integer value
    
    so (x1 - x2) % (v1 - v2) should be equal to zero
    """
        
    
        
    if flag == 0:
        return "NO"
    else:
        return "YES"
