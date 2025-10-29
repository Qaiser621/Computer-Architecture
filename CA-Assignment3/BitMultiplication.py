def bit_multiplication(a, b, signed=False):
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
    n = max(1, aa.bit_length(), bb.bit_length())
    product = 0
    for i in range(n):
        if (bb >> i) & 1:
            product += aa << i
    if signed and sign < 0:
        product = -product
    return product
