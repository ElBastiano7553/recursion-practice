def to_binary(n: int) -> str:
    if n < 0:
        raise ValueError("")
    elif n == 0 or n == 1:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2) 
