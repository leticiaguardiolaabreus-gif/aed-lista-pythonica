def generate_numbers(n: int) -> list[int]:
    """
    Gera uma lista de números de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista [1, 2, ..., n]
    """
    numeros = []

    for i in range(1,n+1):
        if n == 0:
            return []
        else:
            numeros.append(i)
    return numeros
    pass
