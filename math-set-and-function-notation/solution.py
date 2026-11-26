def is_subset(a, b):
   return a.issubset(b)


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    max = values[0]
    for i in values:
        if i > max:
            max = i

    return values.index(max)
