def booths_multiplication(a, b, bits=4):
    def mask(val, bits): return val & ((1 << bits) - 1)
    def to_twos(val, bits): return mask((1 << bits) + val, bits) if val < 0 else mask(val, bits)
    def from_twos(val, bits):
        sign_bit = 1 << (bits - 1)
        return val - (1 << bits) if val & sign_bit else val
    M = to_twos(a, bits)
    Q = to_twos(b, bits)
    A = 0
    Q_1 = 0
    for i in range(bits):
        q0 = Q & 1
        if q0 == 1 and Q_1 == 0:
            A = mask(A - M, bits)
        elif q0 == 0 and Q_1 == 1:
            A = mask(A + M, bits)
        combined = (A << (bits + 1)) | (Q << 1) | Q_1
        old_msb_A = (A >> (bits - 1)) & 1
        combined_shifted = (combined >> 1) | (old_msb_A << (2 * bits))
        A = (combined_shifted >> (bits + 1)) & ((1 << bits) - 1)
        Q = (combined_shifted >> 1) & ((1 << bits) - 1)
        Q_1 = combined_shifted & 1
    product = (A << bits) | Q
    return from_twos(product, 2 * bits)
