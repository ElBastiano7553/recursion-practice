def layer_sum(n: int) -> int:
    if n < 0:
        n = - n
    if n < 10:
        return n
    else:
        return n % 10 + layer_sum(n // 10)
