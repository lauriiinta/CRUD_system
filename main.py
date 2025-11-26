from data import load_presents
from list_CRUD import *

presents = load_presents()

id_counter = 3
while True: #begalinis ciklas, kuris igalina funkcijos veikima vel ir vel
    print_info()
    option = input()
    match option: # vartotojo pasirinkimai ka gali daryti programoje
        case '1':
            print_presents(presents)
        case '2':
            id_counter = create_presents(id_counter, presents)
        case '3':
            edit_presents(presents)
        case '4':
            delete_presents(presents)
        case '5':
            break