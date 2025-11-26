presents = [
            {
                'id': 1,
                "present_title":"Kvepalai",
                "price":70.0,
                "for_who":"mamai"
            },
            {
                'id': 2,
                "present_title":"Zaislai",
                "price":25.0,
                "for_who":"duktereciai"
            },
            {
                'id': 3,
                "present_title":"Saldumynai",
                "price":10.0,
                "for_who":"draugei"
            }
        ]
id_counter = 3
while True: #begalinis ciklas, kuris igalina funkcijos veikima vel ir vel
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti dovanu pasirinkimus")
    print("2. Įtraukti dovana i sarasa")
    print("3. koreguoti dovanas")
    print("4. šalinti dovana")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
    option = input()
    match option: # vartotojo pasirinkimai ka gali daryti programoje
        case '1':
            print("galimi dovanu pasirinkimai:")
            for pres in presents:
                print(f"{pres['id']}. Dovana {pres['for_who']} {pres['present_title']}. Kaina: {pres['price']}")
        case '2':
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
        case '3':
            for pres in presents:
                print(
                    f"{pres['id']}. Dovanos {pres['for_who']} {pres['present_title']}. Kaina: {pres['price']}")
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
        case '4':
            for pres in presents:
                print(
                    f"{pres['id']}. Dovanos {pres['for_who']} {pres['present_title']}. Kaina: {pres['price']}")
            print("iveskite id dovanos kuria norite trinti")
            del_id = input()
            for pres in presents:
                if del_id == str(pres['id']):
                    print(pres)
                    pos = presents.index(pres)
                    del presents[pos]
                    break
        case '5':
            break

