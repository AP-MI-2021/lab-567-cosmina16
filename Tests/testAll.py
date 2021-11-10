from Tests.testCRUD import test_adauga_rezervare, test_sterge_rezervare, test_get_by_id, test_modifica_rezervare


def test_all():
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_get_by_id()
    test_modifica_rezervare()

