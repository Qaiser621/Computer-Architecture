def nonrestoring_division(dividend, divisor, signed=False):
    if divisor == 0:
        raise ZeroDivisionError
    sign_q = 1
    sign_r = 1
    a = dividend
    b = divisor
    if signed:
        if a < 0:
            sign_r = -1
            a = -a
        if b < 0:
            sign_q = -1
            b = -b
    n = max(1, a.bit_length())
    A = 0
    Q = a
    for i in range(n):
        A = (A << 1) | ((Q >> (n - 1)) & 1)
        Q = (Q << 1) & ((1 << n) - 1)
        if A >= 0:
            A = A - b
        else:
            A = A + b
        if A >= 0:
            Q = Q | 1
    quotient = Q * sign_q
    remainder = A
    if remainder < 0:
        remainder = remainder + b
    remainder *= sign_r
    return quotient, remainder
