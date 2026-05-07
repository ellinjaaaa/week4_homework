import json
import sys
import os

shopping_file="shopping.json"

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

