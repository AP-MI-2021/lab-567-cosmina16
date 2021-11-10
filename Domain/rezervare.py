def creeaza_rezervare(ID,nume,clasa,pret,checkin):
    """reprezinta o rezervare
    :param ID:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :return:un dictionar ce reprezinta o rezervare
    """
    return [ID, nume, clasa,pret,checkin]

def get_ID(rezervare):
    """
    da id-ul unei rezervari
    :param rezervare:rezervare
    :return: id-ul rezervarii - string
    """
    return rezervare[0]

def get_nume(rezervare):
    """
    da numele unei rezervari
    :param rezervare:revervare
    :return: numele unei rezervari - id
    """
    return rezervare[1]

def get_clasa(rezervare):
    """
    da clasa unei rezervari
    :param rezervare: rezervare
    :return:clasa unei rezervari
    """
    return rezervare[2]

def get_pret(rezervare):
    """
    da pretul unei rezervari
    :param rezervare:rezervare
    :return:pretul unei rezervari
    """
    return rezervare[3]

def get_checkin(rezervare):
    """
    da starea checkinului unei rezervari
    :param rezervare:rezervare
    :return:checkinul unei rezervari
    """
    return rezervare[4]

def to_string(rezervare):
    return "ID: {}, nume: {}, clasa: {},pret: {}, checkin: {}".format(
        get_ID(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )


