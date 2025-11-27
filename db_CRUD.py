import pymysql

# pip install mysql-connector-python
#pip install pymysql #jei ana neveikia


DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'L@uriuX89',
    'database': 'presents'
}

headers = ['id','present_title','price','for_who']
def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_presents():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from presents")
    rows = cur.fetchall()
    conn.close()
    cur.close()
    presents = []
    for row in rows:
        present = {}
        for i in range(len(headers)):
            present[headers[i]] = row[i]
        presents.append(present)
    return presents

def create_presents(id_counter, presents):
    print("pridedu nauja")
    print("Iveskite dovanos pavadinima")
    present_title = input()
    print("Iveskite dovanos kaina")
    price = float(input())
    print("Iveskite kam dovanosite")
    for_who = input()
    # id_counter += 1
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO `presents` (`present_title`,`price`,`for_who`) VALUES (%s,%s,%s);",
        (present_title, price, for_who)
    )
    conn.commit()
    cur.close()
    conn.close()
    return id_counter

def edit_presents(presents):
    print_presents(presents)
    print("iveskite id dovanos kuria norite redaguoti")
    edit_id = input()
    print("Iveskite dovanos pavadinima")
    present_title = input()
    print("Iveskite kaina")
    price = input()
    print("Iveskite kam skirta dovana")
    for_who = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE `presents` SET `present_title` = %s, `price` =%s,`for_who` = %s WHERE `id` = %s;",
        (present_title, price, for_who, edit_id)
    )
    conn.commit()
    cur.close()
    conn.close()

def delete_presents(presents):
    print_presents(presents)
    print("iveskite id dovanos kuria norite trinti")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM `presents` WHERE `id` = %s;",
        (del_id,) #BŪTINAI REIKIA KABLELIO, KAD TRAKTUOTŲ KAIP TUPPLE, O NE APSKLIAUSTĄ REIKŠMĘ!
    )
    conn.commit()
    cur.close()
    conn.close()

def print_info():
    print("--------------------------------------------------------------------------")
    print("1. Atvaizduoti dovanu pasirinkimus")
    print("2. Įtraukti dovana i sarasa")
    print("3. koreguoti dovanas")
    print("4. šalinti dovana")
    print("5. išeiti iš programos")
    print("-----------------------------Pasirinkite:---------------------------------")
def print_presents(presents):
    presents = load_presents()
    for pres in presents:
        print(
            f"{pres['id']}. Dovana {pres['for_who']} {pres['present_title']}. Kaina: {pres['price']}")