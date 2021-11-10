from Domain.rezervare import get_nume, get_clasa, creeaza_rezervare, get_ID, get_pret, get_checkin


def transformareClasaSuperioara(nume, lista):
    '''
    transforma intr-o clasa superioara rezervarile cu numele citit
    :param nume: numele unei rezervari
    :param lista: lista rezervarilor
    :return: o noua lista transformata cu rezervarile cu un anumit nume la o clasa superioara, restul ramanand nemodificate
    '''
    new_list = []
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == 'economy':
                clasa_noua = 'economy plus'
            else:
                clasa_noua = 'business'
            rezervareNoua = creeaza_rezervare(
                get_ID(rezervare),
                get_nume(rezervare),
                clasa_noua,
                get_pret(rezervare),
                get_checkin(rezervare)
            )
            new_list.append(rezervareNoua)
        else:
            new_list.append(rezervare)
    return new_list