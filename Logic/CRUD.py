from Domain.rezervare import get_ID, creeaza_rezervare


def adauga_rezervare(ID,nume,clasa,pret,checkin,lst_rezervare):
    """
    Adauga o rezervare in lista
    :param ID:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :param lst_rezervare: lista de rezervari
    :return: o noua lista formata din lst_rezervari si noua rezervare adaugata
    """
    rezervare= creeaza_rezervare (ID,nume,clasa,pret,checkin)
    return lst_rezervare+ [rezervare]

def get_by_id(ID, lst_rezervare):
    """
    ia rezervarea cu ID-ul dat
    :param ID:string
    :param lst_rezervare:lista de rezervari
    :return:rezervarea cu ID-ul dat sau none,daca nu exista rezervarea cu Id-ul dat
    """
    rezervare_gasita =[]

    if ID is None:
        return lst_rezervare

    for rezervare in lst_rezervare:
        if get_ID(rezervare)==ID:
            rezervare_gasita = rezervare
    return rezervare_gasita

def sterge_rezervare(ID,lst_rezervare):
    """
    sterge o rezervare din lista
    :param ID:id ul rezervarii pe care vrem sa il stergem
    :param lst_rezervare:lista de rezervari
    :return:noua lista ce nu contine rezervare cu id-ul ID
    """
    lst =[]
    for rezervare in lst_rezervare:
        if get_ID(rezervare) != ID:
            lst.append(rezervare)
    return lst


def modifica_rezervare(ID,nume,clasa,pret,checkin,lst_rezervare):
    """
    modifica o rezervare dupa un id
    :param ID:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :param lst_rezervare:lista de rezervari
    :return:lista modificata
    """
    lst = []
    for rezervare in lst_rezervare:
        if get_ID(rezervare) == ID:
            rezervare_noua = creeaza_rezervare(ID,nume,clasa,pret,checkin)
            lst.append(rezervare_noua)
        else:
            lst.append(rezervare)
    return lst
