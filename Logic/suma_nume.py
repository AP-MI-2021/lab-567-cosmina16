from Domain.rezervare2 import get_nume, get_pret


def suma_nume(lst_rezervare):
    """
    suma preturilor dupa fiecare nume
    :param rezervare: lista cu rezervari
    :return: o lista cu suma preturilor pentru fiecare nume
    """
    try:
        result = {}
        for rezervare in lst_rezervare:
            nume = get_nume(rezervare)
            pret = get_pret(rezervare)
            if nume in result:
                result[nume]= result[nume] + pret
            else:
                result[nume] = pret
        return result
    except ValueError as ve:
        print('Eroare:',ve)