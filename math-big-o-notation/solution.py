def count_comparisons_linear_search(arr, target):
    """
    arr:    a list of numbers
    target: the value being searched for

    Returns:
        (found, comparisons): found is True if target is in arr, False
        otherwise. comparisons is the number of element-to-target
        comparisons actually performed (stop as soon as a match is
        found -- don't keep scanning).
    """
    comparisons = 0
    found = False
    for i in (arr):
        comparisons +=1
        if i==target:
            found = True
            return found , comparisons
        
    return found , comparisons


def count_comparisons_binary_search(sorted_arr, target):
    """
    sorted_arr: a list of numbers, already sorted ascending
    target:     the value being searched for

    Returns:
        (found, comparisons): same shape as count_comparisons_linear_search,
        but using binary search -- each comparison must actually halve
        the remaining search space.
    """
    found = False
    comparisons =0
    low = 0 
    high = len(sorted_arr)-1
    while low <= high:
        comparisons += 1
        mid = (low+high) // 2
        if sorted_arr[mid] == target:
            found = True 
            return found , comparisons
        elif sorted_arr[mid] > target:
            high = mid-1
        elif sorted_arr[mid] < target:
            low = mid+1

    return found , comparisons
