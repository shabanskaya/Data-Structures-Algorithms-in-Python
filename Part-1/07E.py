def is_add_35(n):
    if n == 1:
        return True
    if n < 1:
        return False 
    return is_add_35(n-3) or is_add_35(n-5)

