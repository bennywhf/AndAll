import math
def AndAll(start,end):
    s = start
    zeros_from_right = int(math.log(end-start,2))+1

    s >> zeros_from_right
    s << zeros_from_right
    
    return s & end
