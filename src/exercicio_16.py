def odd_numbers(n: int) -> list[int]:
    """
    Retorna os números ímpares de 1 até n.

    Args:
        n (int): limite superior

    Returns:
        list[int]: lista de números ímpares
    """
    impares = []

    for i in range(1,n+1):
        if i % 2 == 1:
            impares.append(i)
    return impares
    pass
