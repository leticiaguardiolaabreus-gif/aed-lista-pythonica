def add_guests(
    guests: list[str],
    new_guests: list[str]
) -> list[str]:
    """
    Adiciona múltiplos convidados à lista.

    Args:
        guests (list[str]): lista original
        new_guests (list[str]): novos convidados

    Returns:
        list[str]: lista atualizada
    """
    for i in new_guests:
        guests.append(i)
    return guests
    pass
