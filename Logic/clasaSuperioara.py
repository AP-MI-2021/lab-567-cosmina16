from Domain.rezervare import get_name, get_class, get_new_reservation, get_id, get_price, get_checkin


def transformareClasaSuperioara(nume, lista):
    '''
    transforma intr-o clasa superioara rezervarile cu numele citit
    :param nume: numele unei rezervari
    :param lista: lista rezervarilor
    :return: o noua lista transformata cu rezervarile cu un anumit nume la o clasa superioara, restul ramanand nemodificate
    '''
    new_list = []
    for rezervare in lista:
        if get_name(rezervare) == nume:
            if get_class(rezervare) == 'economy':
                clasa_noua = 'economy plus'
            else:
                clasa_noua = 'business'
            rezervareNoua = get_new_reservation(
                get_id(rezervare),
                get_name(rezervare),
                clasa_noua,
                get_price(rezervare),
                get_checkin(rezervare)
            )
            new_list.append(rezervareNoua)
        else:
            new_list.append(rezervare)
    return new_list