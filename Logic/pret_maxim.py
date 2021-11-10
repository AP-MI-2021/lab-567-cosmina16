from Domain.rezervare import get_clasa, get_pret


def pret_max_clasa(lst_rezervare):
    """
    functia va determina maximul pretului pentru fiecare clasa
    :param lst_rezervare: lista de rezervari
    :return: returneaza maximul pret pt fiecare clasa
    """
    try:
        max_economy = 0
        max_economy_plus = 0
        max_business = 0
        for rezervare in lst_rezervare:
            if get_clasa(rezervare) == 'economy':
                if max_economy < get_pret(rezervare):
                    max_economy = get_pret(rezervare)
            elif get_clasa(rezervare) == 'economy plus':
                if max_economy_plus < get_pret(rezervare):
                    max_economy_plus = get_pret(rezervare)
            else:
                if max_business < get_pret(rezervare):
                    max_business = get_pret(rezervare)
        return max_economy, max_economy_plus, max_business
    except ValueError as ve:
        print('Eroare:', ve)
