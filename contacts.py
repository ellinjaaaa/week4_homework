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
                                        
def add_contact(contacts, name, phone):
    '''
    Pievieno jaunu kontaktu ar input(). Apstrādā kļūdas: tukšums vārda/tel. vietā, tel.nr. īsāks par 8 rakstzīmēm, tālr. nr.
    nesastāv no cipariem vai, ja sākas ar +, tad turpmāk jāsastāv no cipariem, pastāv dublikāts tālr. nr.
    '''
    name=name.strip() #Nav atstarpju sākumā vai beigās, taču pa vidu paliek.
    phone=phone.strip()

    if not name or not phone:
        print("Nevar būt tukša ievade.")
        return False
    
    if len(phone)<8:
        print("Tālruņa nr. jābūt vismaz 8 rakstzīmes garam.")
        return False
    
    if not (phone.isdigit() or (phone.startswith("+") and phone[1:].isdigit())): #Tālr. nr. jāsastāv nk cipariem - ja tomēr
        print("Tālruņa nr. jasastāv no cipariem.") #uzrakstīts arī valsts kods, spēj apstrādāt situāciju, ka sākas ar +, savukārt, pēc tam cipari.
        return False

    for c in contacts:
        if c["phone"] == phone:
            print("Šāds tālruņa nr. jau pastāv.")
            return False
    
    contacts.append({"name":name, "phone":phone})

    print(f"Pievienots: {name} ({phone})")

    return True

def list_contacts(contacts):
    '''
    Atgriež sanumurētu sarakstu ar vārdu un tālr. nr. Citādāk - nav kontaktu.
    '''
    if not contacts:
        print("Nav kontaktu.")
        return False

    for a, b in enumerate(contacts):
        print(f"{a+1}. {b['name']} - {b['phone']}")

    return True

def search_contact(contacts, find):
    '''
    Atrod kontaktu pēc vārda. Ja atrod - sanumurē, pieraksta vārdu un tālr. nr.
    Citādāk - tāda kontakta nav.
    '''
    results=0
    
    for a, b in enumerate(contacts):
        if find.lower() in b['name'].lower():
            print(f"{a+1}. {b['name']} - {b['phone']}")
            results+=1
    
    if results==0:
        print ("Tāda kontakta nav.")