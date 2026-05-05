import json
import sys
import os

contacts_file="contacts.json"

def load_contacts():
    '''
    Nolasa kontaktus no JSON faila, pārveidojot Python failā. Ja fails neeksistē vai bojāts, atgriež tukšu sarakstu.
    '''
    if not os.path.exists(contacts_file):
        return []
    try:
        with open(contacts_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError): #Ja fails bojāts kādā veidā, tiek atgriezts tukšs saraksts.
        return []
    
def save_contacts(contacts):
    '''
    Saglabā kontaktu sarakstu; Python -> JSON. Ja kļūda - paziņojums ar kļūdu.
    '''
    try:
        with open(contacts_file, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Nevar saglabāt failu: {e}.") #Paglābj no programmas crashošanas vai citām kļūdām, 
    #pie reizes norādot kļūdu (kas saglabāta, kā mainīgais e).
                                        
def add_contact(list_contacts):
    '''
    Pievieno jaunu kontaktu ar input(). Apstrādā kļūdas: tukšums vārda/tel. vietā, tel.nr. īsāks par 8 rakstzīmēm,
    pastāv dublikāts tālr. nr.
    '''
    name=input("Ievadiet kontakta vārdu: ").strip() #.strip() noņem atstarpes sākumā un beigās, bet ne pa vidu
    phone=input("Ievadiet tālruņa nr.: ").strip()

    if not name or not phone:
        print("Nevar būt tukša ievade.")
        return False
    
    if len(phone)<8:
        print("Nederīgs tālruņa nr.")
        return False

    for c in list_contacts:
        if c["Tel."] == phone:
            print("Šāds tālruņa nr. jau pastāv.")
            return False
    
    list_contacts.append({"Vārds":name, "Tel.":phone})

    print(f"Kontakts '{name}' ir pievienots.")

    return True

#def list_contacts():
#def search_contact():