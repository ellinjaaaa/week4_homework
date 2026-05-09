import sys

from storage import load_shopping, save_shopping, add_shopping, list_shopping, total_shopping, clear_shopping, load_prices, save_prices, get_price, set_price

def shop():
    '''
    Apvieno visas iepriekš uzrakstītās komandas vienā funkcijā. Ar sys.argv palīdzību lietotājs ievada nepieciešamo komandu 
    izpildei ar nepiciešamajām vērtībām. Ja neatpazīst komandu, izvadē: "Nezināma komanda".
    '''
    products=load_shopping()

    if len(sys.argv)<2:
        print("Komandas: add (pievienot), list (saraksts), total (kopsumma), clear(notīrīt visu sarakstu)")
        return
    
    cmd=sys.argv[1]

    if cmd=="add":
        if len(sys.argv)<4:
            print("Add komanda: add \"Produkts\" Daudzums") #\, lai varētu izmantot tādas pašas pēdiņas iekšpusē.
            return
        
        name=sys.argv[2]
        qty=sys.argv[3]

        price=get_price(name) #Cena meklēta datu bāzē.

        #Ja cena nav atrasta
        if price is None:
            print("Cena nav zināma")

            try:
                price=float(input("Ievadi cenu: "))

            except ValueError:
                print("Nepareiza cena.")
                return
            
            if price<=0:
                print("Cenai jābūt pozitīvai.")
                return
            
            set_price(name, price)

            print(f"Cena saglabāta: {name} ({price:.2f} EUR)")

        #Ja cena ir atrasta
        else:
            print(f"Atrasta cena: {price:.2f} EUR/gab.")
            choice=input("[A]kceptēt / [M]ainīt?").lower()

            if choice=="m":

                try:
                    price=float(input("Jaunā cena: "))

                except ValueError:
                    print("Nepareiza cena.")
                    return
                
                if price<=0:
                    print("Cenai jābūt pozitīvai.")
                    return
            
                set_price(name, price)

                print(f"Cena atjaunināta: {name} - {price:.2f} EUR")

        #Pievieno produktu iepirkumu sarakstam
        if add_shopping(products, name, qty, price):
            save_shopping(products)

    elif cmd=="list":
        print("Produkti:")
        list_shopping(products)

    elif cmd=="total":
        total_shopping(products)

    elif cmd=="clear":
        clear_shopping(products)
        save_shopping(products)

    else:
        print("Nezināma komanda.")

if __name__=="__main__":
    shop()