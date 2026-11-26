def factorial(n):
    total = 1
    for i in range(1 , n+1):
        total *= i
    return total
        


def n_choose_k(n, k):
    """
    n, k: non-negative integers, 0 <= k <= n

    Returns:
        C(n, k) = n! / (k! * (n - k)!), the number of size-k subsets of
        an n-element set, as an integer.
    """
    return factorial(n)//(factorial(k)*(factorial(n-k)))
