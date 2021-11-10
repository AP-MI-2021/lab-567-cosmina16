from Domain.rezervare import get_ID, get_nume, get_clasa, get_pret, get_checkin
from Logic.CRUD import adauga_rezervare, sterge_rezervare, get_by_id, modifica_rezervare


def test_adauga_rezervare():
    rezervare= adauga_rezervare("1", "Ada", "economy", 1000.01, "da", [])

    assert len(rezervare) == 1
    assert get_ID(rezervare[0]) == "1"
    assert get_nume(rezervare[0]) == "Ada"
    assert get_clasa(rezervare[0]) == "economy"
    assert get_pret(rezervare[0]) == 1000.01
    assert get_checkin(rezervare[0]) == "da"


def test_sterge_rezervare():
    lst = []
    lst = adauga_rezervare("1", "Ada", "economy", 100.01, "da", lst)
    lst = adauga_rezervare("2", "Ana", "economy plus", 200.02, "nu", lst)
    lst = sterge_rezervare("2", lst)

    assert get_by_id("1", lst) is not None
    assert get_by_id("2", lst) is None

def test_get_by_id():
    lst = []
    lst = adauga_rezervare("1", "ada", "ec plus", 24.95, "da", lst)
    lst = adauga_rezervare("2", "ana", "ec", 29.71, "nu", lst)

    assert get_by_id("2", lst) is not None
    assert get_by_id("5", lst) is None

def test_modifica_rezervare():
    lst = []
    lst = adauga_rezervare("1", "ana", "ec", 24.95, "da", lst)
    lst = adauga_rezervare("2", "ada", "ec plus", 29.71, "nu", lst)
    lst =modifica_rezervare("1", "ana", "ec", 24.99, "da", lst)
    rezervare_modificata = get_by_id("1", lst)

    assert get_pret(rezervare_modificata) == 24.99