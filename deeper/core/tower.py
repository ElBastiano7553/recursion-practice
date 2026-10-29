def hanoi(n: int, start: str, end: str, intermediate: str) -> None:
    if n < 0:
        raise ValueError("Invalid argument")
    if n == 0:
        return
    hanoi(n - 1, start, intermediate, end)
    print(f"disk {n}: {start} -> {end}")
    hanoi(n - 1, intermediate, end, start)