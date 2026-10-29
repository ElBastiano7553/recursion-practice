def countdown_beacon(n: int) -> str:
    if n < 0:
        raise ValueError("")
    elif n == 0:
        return str(0)
    else:
        return str(n) + "," + countdown_beacon(n - 1)