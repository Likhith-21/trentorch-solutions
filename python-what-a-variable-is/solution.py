def compute_total(price: float, quantity: int) -> float:
    subtotal = price * quantity
    tax = subtotal * 0.08
    subtotal += tax
    return subtotal


def swap_two_variables(a, b):
    a , b = b ,a 
    return a,b
