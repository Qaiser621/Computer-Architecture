def bitpair_multiplication(a, b, signed=False):
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
    q_extended = bb << 1
    n = max(1, aa.bit_length(), bb.bit_length())
    product = 0
    for i in range((n + 1) // 2 + 1):
        triple = (q_extended >> (2 * i)) & 0b111
        if triple in (0b000, 0b111):
            factor = 0
        elif triple in (0b001, 0b010):
            factor = 1
        elif triple == 0b011:
            factor = 2
        elif triple == 0b100:
            factor = -2
        elif triple in (0b101, 0b110):
            factor = -1
        else:
            factor = 0
        product += (aa * factor) << (2 * i)
    if signed and sign < 0:
        product = -product
    return product
