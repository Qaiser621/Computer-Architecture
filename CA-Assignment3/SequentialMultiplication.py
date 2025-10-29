def mask(val, bits):
    return val & ((1 << bits) - 1)

def sequential_multiplication(a, b, bits=None, signed=False):
    sign = 1
    aa = a
    bb = b
    if signed:
        if a < 0:
            sign *= -1
            aa = -aa
        if b < 0:
            sign *= -1
            bb = -bb
    if bits is None:
        bits = max(1, aa.bit_length(), bb.bit_length())
    n = bits
    combined = bb  # lower n bits = Q, upper n bits = A (initially 0)
    M_shift = aa << n
    for _ in range(n):
        if combined & 1:
            combined = combined + M_shift
        combined = combined >> 1
    product = combined & ((1 << (2 * n)) - 1)
    if signed and sign < 0:
        product = -product
    return product
