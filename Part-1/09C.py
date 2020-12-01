
def find_root(f, a, b, tol):
    x = (a+b)/2
    while (b-a) > tol:
        x = (a+b)/2
        if abs(f(x)) < 10**(-6):
            return x
        elif f(x)*f(a)<0:
            b = x
        else:
            a = x
    else:
        return x
    
