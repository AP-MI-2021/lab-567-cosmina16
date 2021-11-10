from Domain.rezervare import get_nume


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
            if getClasa(rezervare) == 'economy':
                clasa_noua = 'economy plus'
            else:
                clasa_noua = 'business'
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                clasa_noua,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            new_list.append(rezervareNoua)
        else:
            new_list.append(rezervare)
    return new_list