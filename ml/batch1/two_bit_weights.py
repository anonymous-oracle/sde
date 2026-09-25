def pack_2bit_weights(v0, v1, v2, v3):
    packed_byte = 0
    packed_byte = (v0) | (v1 << 2) | (v2 << 4) | (v3 << 6)
    return packed_byte

def unpack_2bit_weights(packed_byte):
    return packed_byte & 3, (packed_byte >> 2) & 3, (packed_byte >> 4) & 3, (packed_byte >> 6) & 3