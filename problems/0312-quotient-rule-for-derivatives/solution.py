def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    try:
        return (gradient(g_coeffs, x) * fn(h_coeffs, x) - fn(g_coeffs, x) * gradient(h_coeffs, x)) / (fn(h_coeffs, x) ** 2)
    except ZeroDivisionError:
        return -1

def fn(coeffs: list, x: float) -> float:
    n = len(coeffs)
    result = 0
    for i, v in enumerate(coeffs):
        result += v * (x ** (n -i -1))
    return result
    
def gradient(coeffs: list, x: float) -> float:
    n = len(coeffs)
    result = 0
    for i, v in enumerate(coeffs):
        result += (n - i - 1) * v * (x ** (n - i - 2))
    return result
