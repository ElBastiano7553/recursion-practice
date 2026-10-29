def deepest_digit(n: int) -> int:
    if n < 0:
        n = -n
    if n < 10:
        return n
    last = n % 10
    rest = deepest_digit(n // 10)
    if last < rest:
        return rest
    else:
        return last