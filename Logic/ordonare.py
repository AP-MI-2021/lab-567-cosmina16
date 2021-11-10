from Domain.rezervare import get_pret

def pret(rezervare):
    """
    criterul de ordonare
    :param rezervare: rezervare
    :return: pretul rezervarii
    """
    return get_pret(rezervare)

def ordonare_rezervare(lst_rezervare):
    return sorted(lst_rezervare,key=pret, Reverse=True)
