def create_causal_mask(seq_len):

    mask_matrix = [[] for i in range(seq_len)]
    for i in range(seq_len):
        for j in range(seq_len):
            if j <= i:
                mask_matrix[i].append(0)
            else:
                mask_matrix[i].append(float('-inf'))

    return mask_matrix

if __name__ == "__main__":
    print(create_causal_mask(4))