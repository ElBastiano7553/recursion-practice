def echo(n: int) -> int:
    if n < 0:
        raise ValueError("")
    elif n == 0 or n == 1:
        return n
    else:
        n = echo(n - 1) + echo(n - 2)
        return n