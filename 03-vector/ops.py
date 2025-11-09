def scalar_vector_mult(alpha, v):
    return [alpha * v[i] for i in range(len(v))]


def add2(v, w):
    return [v[0] + w[0], v[1] + w[1]]
