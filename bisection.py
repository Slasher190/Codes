#bisection formula to find real root of equation
import math
def bisection(function,a,b):
    start = a
    end = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif (function(a)*function(b)>0):
        print("Error no root available within the interval")
    else :
        mid = start + (end - start)/2.0
        while abs(start - end) > 10**(-7):
            if function(mid) == 0:
                return mid
            elif (function(start)*function(mid) < 0):
                end = mid
            else : 
                start = mid
            mid = start + (end - start)/2.0
        return mid

def f(x):
    return math.pow(x,3) - 2*x - 5

if __name__ == "__main__":
    print(bisection(f,1,1000))
        
