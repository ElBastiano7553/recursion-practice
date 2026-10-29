def depth_sum(n: int) -> int:
    if  n < 0:
        raise ValueError("")
    else:
            n = n + depth_sum(n - 1)