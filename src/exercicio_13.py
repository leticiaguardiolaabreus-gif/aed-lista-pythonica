def shrink_guest_list(guests: list[str]) -> list[str]:
    """
    Reduz a lista para apenas dois convidados.

    Args:
        guests (list[str]): lista original

    Returns:
        list[str]: lista com apenas dois elementos
    """
    lista =[]
    contador =0

    for i in guests:
        if contador <2:
            lista.append(i)
            contador +=1
        else:
            break
    return lista
    pass
