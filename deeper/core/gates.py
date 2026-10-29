def gate_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        n = b
        b = a % b
        return gate_gcd(n, b)
