def creeaza_rezervare(ID,nume,clasa,pret,checkin):
    """
    creeaza un dictionar ce reprezinta o rezervare
    :param ID:string
    :param nume:string
    :param clasa:string
    :param pret:float
    :param checkin:string
    :return:un dictionar ce reprezinta o rezervare
    """
    return {
        "id": ID,
        "titlu": nume,
        "gen": clasa,
        "pret": pret,
        "reducere": checkin
    }

def get_ID(rezervare):
    """
    da id-ul unei rezervari
    :param rezervare:rezervare
    :return: id-ul rezervarii - string
    """
    return rezervare["ID"]

def get_nume(rezervare):
    """
    da numele unei rezervari
    :param rezervare:revervare
    :return: numele unei rezervari - id
    """
    return rezervare["nume"]

def get_clasa(rezervare):
    """
    da clasa unei rezervari
    :param rezervare: rezervare
    :return:clasa unei rezervari
    """
    return rezervare["clasa"]

def get_pret(rezervare):
    """
    da pretul unei rezervari
    :param rezervare:rezervare
    :return:pretul unei rezervari
    """
    return rezervare["pret"]

def get_checkin(rezervare):
    """
    da starea checkinului unei rezervari
    :param rezervare:rezervare
    :return:checkinul unei rezervari
    """
    return rezervare["checkin"]

def to_string(rezervare):
    return "ID: {}, nume: {}, clasa: {},pret: {}, checkin: {}".format(
        get_ID(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin(rezervare)
    )
