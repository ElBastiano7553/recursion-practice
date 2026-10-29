def oxygen(n: int) -> int:
    if n < 0:
        raise ValueError("")
    else: 
        n = n * oxygen(n - 1)
