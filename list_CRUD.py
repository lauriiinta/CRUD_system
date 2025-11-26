def print_presents(presents):
    for pres in presents:
        print(
            f"{pres['id']}. Dovana {pres['for_who']} {pres['present_title']}. Kaina: {pres['price']}")

def delete_presents(presents):
    print_presents(presents)
    print("iveskite id dovanos kuria norite trinti")
    del_id = input()
    for pres in presents:
        if del_id == str(pres['id']):
            print(pres)
            pos = presents.index(pres)
            del presents[pos]
            break

def create_presents(id_counter, presents):
    print("pridedu nauja")
    print("Iveskite dovanos pavadinima")
    present_title= input()
    print("Iveskite dovanos kaina")
    price = float(input())
    print("Iveskite kam dovanosite")
    for_who = input()
    id_counter += 1
    pres = {'id': id_counter, "present_title": present_title, "price": price, "for_who": for_who}
    presents.append(pres)
    return id_counter

def edit_presents(presents):
    print_presents(presents)
    print("iveskite id dovanos kuria norite redaguoti")
    edit_id = input()
    for pres in presents:
        if edit_id == str(pres['id']):
            print("Iveskite dovanos pavadinima")
            pres['present_title'] = input()
            print("Iveskite kaina")
            pres['price'] = float(input())
            print("Iveskite kam skirta dovana")
            pres['for_who'] = input()
            break

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti dovanu pasirinkimus")
    print("2. Įtraukti dovana i sarasa")
    print("3. koreguoti dovanas")
    print("4. šalinti dovana")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")