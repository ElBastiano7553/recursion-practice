def signal_power(x: int, n: int) -> float:
    if x == 0 and n == 0:
        raise ValueError("")
    elif n <= 0:
        return 1 / (x**n)    
    else:
        return x**n