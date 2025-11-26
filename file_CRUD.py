import csv

headers = ['id','present_title','price','for_who']
def load_presents():
    with open("presents.csv",mode='r',encoding='utf-8') as file:
        return list(csv.DictReader(file))

def save_presents(presents):
    with open('presents.csv',mode='w',newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(presents)

def create_presents(id_counter, presents):
    print("pridedu nauja")
    print("Iveskite dovanos pavadinima")
    present_title = input()
    print("Iveskite dovanos kaina")
    price = float(input())
    print("Iveskite kam dovanosite")
    for_who = input()
    id_counter += 1
    pres = {'id': id_counter, "present_title": present_title, "price": price, "for_who": for_who}
    presents.append(pres)
    save_presents(presents)
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
    save_presents(presents)

def delete_presents(presents):
    print_presents(presents)
    print("iveskite id dovanos kuria norite trinti")
    del_id = input()
    for pres in presents:
        if del_id == str(pres['id']):
            pos = presents.index(pres)
            del presents[pos]
            break
    save_presents(presents)


def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti dovanu pasirinkimus")
    print("2. Įtraukti dovana i sarasa")
    print("3. koreguoti dovanas")
    print("4. šalinti dovanas")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
def print_presents(presents):
    for pres in presents:
        print(
            f"{pres['id']}. Dovana {pres['for_who']} {pres['present_title']}. Kaina {pres['price']}")
