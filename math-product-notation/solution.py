def product(f, lo, hi):
    product = 1
    for i in range(lo , hi+1):
        product *= f(i)
    return product
