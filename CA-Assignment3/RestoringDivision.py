def restoring_division(dividend, divisor, signed=False):
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
    R = 0
    Q_val = 0
    for i in reversed(range(n)):
        R = (R << 1) | ((a >> i) & 1)
        if R >= b:
            R = R - b
            Q_val = Q_val | (1 << i)
    quotient = Q_val * sign_q
    remainder = R * sign_r
    return quotient, remainder
