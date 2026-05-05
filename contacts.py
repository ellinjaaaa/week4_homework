import json
import sys
import os

contacts_file="contacts.json"

def load_contacts():
    '''
    Nolasa kontaktus no JSON faila, pārveidojot Python failā. Ja fails neeksistē, atgriež tukšu sarakstu.
    '''
    if not os.path.exists(contacts_file):
        return []
    try:
        with open(contacts_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError): #Ja fails bojāts kādā veidā, tiek atgriezts tukšs saraksts.
        return []