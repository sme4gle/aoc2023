def read_input(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return [l.strip() for l in f.readlines()]
