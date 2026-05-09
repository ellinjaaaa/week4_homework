import json #import sys būs vajadzīgs shop.py, tā kā tur būs CLI.
import os

shopping_file="shopping.json"

prices_file="prices.json"

def load_shopping():
    '''
    Nolasa produktus no JSON faila, pārveidojot Python failā. Ja fails neeksistē vai bojāts, atgriež tukšu sarakstu.
    '''
    if not os.path.exists(shopping_file):
        return []
    try:
        with open(shopping_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError): #Ja fails bojāts kādā veidā, tiek atgriezts tukšs saraksts.
        return []

def load_prices():
    '''
    Nolasa cenas no JSON faila, pārveidojot Python failā. Ja fails neeksistē vai bojāts, atgriež tukšu sarakstu.
    '''
    if not os.path.exists(prices_file):
        return []
    try:
        with open(prices_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError): #Ja fails bojāts kādā veidā, tiek atgriezts tukšs saraksts.
        return []
    
def save_shopping(products):
    '''
    Saglabā produktu sarakstu; Python -> JSON. Ja kļūda - paziņojums ar kļūdu.
    '''
    try:
        with open(shopping_file, "w", encoding="utf-8") as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Nevar saglabāt failu: {e}.") #Paglābj no programmas crashošanas vai citām kļūdām, 
    #pie reizes norādot kļūdu (kas saglabāta, kā mainīgais e).

def save_prices(prices):
    '''
    Saglabā cenu sarakstu; Python -> JSON. Ja kļūda - paziņojums ar kļūdu.
    '''
    try:
        with open(prices_file, "w", encoding="utf-8") as f:
            json.dump(prices, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Nevar saglabāt failu: {e}.") #Paglābj no programmas crashošanas vai citām kļūdām, 
    #pie reizes norādot kļūdu (kas saglabāta, kā mainīgais e).

def add_shopping(products, name, qty, price):
    '''
    Pievieno jaunu produktu, izmantojot products sarakstu. Ja neparādās kļūdas - tukšums vārda/cenas vietā, cena nav skaitlis 
    vai tā ir negatīva -, produkts tiek pievienots sarakstam, kopā ar cenu, vārdnīcas formā. 
    '''
    name=name.strip() #Nav atstarpju sākumā vai beigās, taču pa vidu paliek.
    price=price.strip()
    qty=qty.strip()

    if not name or not qty or not price: #Lai nav tukšu vērtību.
        print("Nevar būt tukša ievade.")
        return False
    
    try:
        qty=int(qty)
        price=float(price) #Cenai jābūt skaitlim.
    except ValueError:
        print("Daudzumam un/vai cenai jābūt skaitlim.")
        return False
    
    if price<=0: #Cenai jābūt pozitīvai.
        print("Cena nevar būt negatīva.")
        return False
    
    if qty<=0: #Daudzumam jābūt pozitīvam.
        print("Daudzums nevar būt negatīvs.")
        return False
    
    products.append({"name":name, "qty":qty, "price":price})

    total_for_same=qty*price

    print(f"Pievienots: {name} x {qty} ({price:.2f} EUR/gab.) = {total_for_same:.2f} EUR") #Atstāj 2 ciparus aiz komata jebkurai cenai (parādoties tekstam, nevis json failā).

    return True

def list_shopping(products):
    '''
    Atgriež sanumurētu sarakstu ar produktiem un cenām. Citādāk - nav produktu.
    '''
    if not products:
        print("Nav produktu.")
        return False

    for a, product in enumerate(products):
        print(f"{a+1}. {product['name']} x {product['qty']} - {product['price']:.2f} EUR/gab. - {(product['qty']*product['price']):.2f} EUR")

    return True

def total_shopping(products):
    '''
    Ar summu tiek sasummētas produktu cenas ar for cikla palīdzību. Rezultāts noapaļots - 2 cipari aiz komata.
    Ja nav produktu, tiek izvadīts ziņojums par to.
    '''
    if not products:
        print("Nav produktu.")
        return False

    total=sum((p['price']*p['qty']) for p in products) #izmantota summēšana ar for ciklu vienā rindā

    all=sum(p['qty'] for p in products)

    tog=len(products)

    print(f"Kopā: {total:.2f} EUR ({all} vienības, {tog} produkti)")

    return True

def clear_shopping(products):
    '''
    Notīra produktu sarakstu.
    '''
    if not products:
        print("Nav produktu.")
        return False
    
    products.clear()
    print("Saraksts notīrīts.")

    return True

def get_price(products, name):
    '''
    Atrod cenu pēc produkta vārda. Citādāk - tāda produkta nav.
    '''
    if not products:
        print("Nav produktu.")
        return False

    if not name:
        print("Cena nav zināma.")
        return

    for p in products:
        if name.lower()==p['name'].lower():
            print(f"Atrasts/a: {p['price']} EUR")
            return True

    print("Tāda produkta nav.")
    return False

def set_price(name, qty, price):
    '''
    Apstiprina vai maina produkta cenu.
    '''
    text=input("[A]kceptēt / [M]ainīt?")

    if not text:
        print("Lūdzu, izvēlies [A]kceptēt / [M]ainīt?")
        return False

    if text.lower()=="a":
        print(f"Pievienots: {name} x {qty} ({price} EUR/gab.) = {qty*price} EUR")
        return True

    if text.lower()== "m":
        try:
            new_price=float(input("Jaunā cena: "))
        
        except ValueError:
            print("Nepareizi ievadīta cena.")
            return False
        
        if new_price<=0:
            print("Cenai jābūt pozitīvai.")
            return False

        print(f"Cena autjaunināta: {name} - {new_price} EUR")
        print(f"Pievienots: {name} x {qty} ({new_price} EUR/gab.) = {qty*new_price} EUR")

        return True
    
    print("Nesaprotama izvēle.")
    return False