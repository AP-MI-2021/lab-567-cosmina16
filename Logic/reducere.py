from Domain.rezervare import get_checkin, get_pret, creeaza_rezervare, get_ID, get_nume, get_clasa


def reduce_pret_checkin(lst_rezervare,procent):
    """
    functia verifica daca checkin-ul unei rezervari ste 'da' si atunci aplica  o reducere
    :param lst_rezervare:
    :param procent:
    :return:
    """
    if not( 0 <= procent <= 100):
        raise ValueError("procentajul dat trebuie sa fie intre 0 si 100")
    result =[]
    for rezervare in lst_rezervare:
        if 'da' in get_checkin(rezervare):
            pret_nou= get_pret(rezervare)* (100 - procent) /100
            result.append(creeaza_rezervare(
                get_ID(rezervare),
                get_nume(rezervare),
                get_clasa(rezervare),
                pret_nou,
                get_checkin(rezervare)
            ))
        else:
            result.append(rezervare)
    return result


