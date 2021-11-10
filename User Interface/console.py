from Domain.rezervare import to_string, get_ID, get_nume, get_clasa, get_pret, get_checkin, creeaza_rezervare
from Logic.CRUD import adauga_rezervare, get_by_id, modifica_rezervare, sterge_rezervare
from Logic.ordonare import ordonare_rezervare
from Logic.pret_maxim import pret_max_clasa
from Logic.reducere import reduce_pret_checkin


def handle_add(lst_rezervare):
    try:
        ID = int(input('Dati id ul unei rezervari'))
        nume = input('dati numele rezervarii ')
        clasa = input('dati clasa rezervarii ')
        pret = float(input('dati pretul rezervarii '))
        checkin = input('dati starea rezervarii: ')
        return adauga_rezervare(ID,nume,clasa,pret,checkin)
    except ValueError as ve:
        print('Eroare', ve)
    return lst_rezervare

def handle_show_all(rezervari):
    for rezervare in rezervari:
        print(to_string(rezervare))

def handle_show_details(rezervare):
    id_rezervare = int(input('dati id-u rezervarii pentru care doriti detalii: '))
    rezervare =  get_by_id(rezervare, id_rezervare)
    print(f'Nume: {get_nume(rezervare)}')
    print(f'Clasa: {get_clasa(rezervare)}')
    print(f'pret: {get_pret(rezervare)}')
    print(f'checkin: {get_checkin(rezervare)}')

def handle_update(lst_rezervare):
    try:
        id_rezervare= input("Dati id-ul rezervarii ce trebuie modificata: ")
        nume = input("Dati noul nume al rezervarii : ")
        clasa = input("Dati noua clasa a rezervarii: ")
        pret = float(input("Dati noul pret al rezervarii: "))
        checkin = input("Dati noul checkin al rezervariit: ")
        return modifica_rezervare(lst_rezervare,creeaza_rezervare(id_rezervare, nume, clasa, pret, checkin))
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_rezervare

def handle_delete(lst_rezervare):
    try:
        id_rezervare = int(input("Dati id-ul vanzarii ce trebuie sters: "))
        lst_rezervare=sterge_rezervare(id_rezervare, lst_rezervare)
        print ('stergerea a fost efectuata cu succes')
        return lst_rezervare
    except ValueError as ve:
        print("Eroare: ", ve)
    return lst_rezervare



def handle_crud(lst_rezervare):
        print("1. Adaugare rezervare.")
        print("2. Modificare rezervare.")
        print("3. Stergere rezervare.")
        print("x. Iesire")
        print('a. Afisare')
        print('b. detalii REZERVARE')
        print('b. revenire')

        optiune = input('optiunea aleasa este: ')
        if optiune == '1' :
            lst_rezervare =handle_add(lst_rezervare)
        elif optiune == '2' :
            lst_rezervare =handle_update(lst_rezervare)
        elif optiune == '3' :
            lst_rezervare =handle_delete(lst_rezervare)
        elif optiune == 'a':
            handle_show_all(lst_rezervare)
        elif optiune == 'd':
            handle_show_details(lst_rezervare)
        # elif optiune == 'b':
        #    break
        else:
            print('optiune invalida')
        return lst_rezervare

def handle_reducere(rezervare):
    try:
        procentaj_reducere=int(input("Dati un procentaj de reducere(0-100):"))
        reducere = reduce_pret_checkin(rezervare, procentaj_reducere)

        print("pretul rezervarilor a fost redus cu succes")
    except ValueError as ve:
        print('Eroare:',ve)
    return rezervare

def handle_ordonare(rezervare):
    try:
        rezervare = ordonare_rezervare(rezervare)
    except ValueError as ve:
        print('Eroare:', ve)
    return rezervare

def handle_pret_max(rezervare):
    try:
        rezervare = pret_max_clasa(rezervare)
    except ValueError as ve:
        print('Eroare:',ve)
    return rezervare

def show_menu():
    print('1. crud')
    print('3. Reducere pret pntru cei cu checkinul facut')
    print('4. Determina pretul maxim pentru fiecare clasa')
    print('5. Ordoneaza descrescator in functie de pret')
    print ('z.Undo')
    print('y. Redo')
    print('x. Exit')

def handle_new_list(list_versions,current_version, rezervare):
    while current_version<len(list_versions) - 1:
        list_versions.pop()
    list_versions.appendd(rezervare)
    current_version += 1
    return list_versions, current_version

def handle_undo(list_versions,current_version):
    if current_version <1:
        print('NU se mai poate face undo')
        return
    current_version -=1
    return list_versions[current_version], current_version


def handle_redo(list_versions,current_version):
    if current_version == len(list_versions)-1:
        print('NU se mai poate face redo')
        return
    current_version += 1
    return list_versions[current_version], current_version

def run_ui(rezervare):

    list_versions = [rezervare]
    current_version = 0

    while True:
        show_menu()
        optiune = input('Optiunea aleasa: ')
        if optiune =='1':
            rezervare = handle_crud(rezervare)
            list_versions, current_version=handle_new_list(list_versions, current_version, rezervare)
        elif optiune == '3':
            rezervare =handle_reducere(rezervare)
            list_versions, current_version= handle_new_list(list_versions, current_version, rezervare)
        elif optiune == '4':
            rezervare =handle_pret_max(rezervare)
            list_versions, current_version= handle_new_list(list_versions, current_version, rezervare)
        elif optiune == '5':
            rezervare =handle_ordonare(rezervare)
            list_versions, current_version=handle_new_list(list_versions, current_version, rezervare)
        elif optiune == 'z':
            rezervare, current_version =handle_undo(list_versions, current_version)
        elif optiune == 'y':
            rezervare, current_version =handle_redo(list_versions, current_version)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida')
    return rezervare



