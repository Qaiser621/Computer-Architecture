def mask(val, bits):
    return val & ((1 << bits) - 1)

def to_twos(val, bits):
    if val < 0:
        return mask((1 << bits) + val, bits)
    else:
        return mask(val, bits)

def from_twos(val, bits):
    sign_bit = 1 << (bits - 1)
    if val & sign_bit:
        return val - (1 << bits)
    else:
        return val

def bin_str(val, bits):
    return format(mask(val, bits), '0{}b'.format(bits))

def add(a, b, bits=4, signed=False):
    A = to_twos(a, bits)
    B = to_twos(b, bits)
    raw = A + B
    result_twos = mask(raw, bits)
    if signed:
        result = from_twos(result_twos, bits)
        overflow = ((a >= 0 and b >= 0 and result < 0) or (a < 0 and b < 0 and result >= 0))
    else:
        result = result_twos
        overflow = (raw >> bits) != 0
    return result, bin_str(result_twos, bits), overflow

def subtract(a, b, bits=4, signed=False):
    return add(a, -b, bits, signed)
