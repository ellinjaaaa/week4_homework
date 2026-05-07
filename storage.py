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