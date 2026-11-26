def summation(f, lo, hi):
    total = 0
    if hi < lo:
        return 0
    else:
        for i in range(lo , hi+1):
            total += f(i)
    return total
