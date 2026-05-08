import sys

from storage import load_shopping, save_shopping, add_shopping, list_shopping, total_shopping, clear_shopping

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
            print("Add komanda: add \"Produkts\" Cena") #\, lai varētu izmantot tādas pašas pēdiņas iekšpusē.
            return
        
        if add_shopping(products, sys.argv[2], sys.argv[3]): #If, jo funkcijā return True/False - saglabās, tikai ja True.
            save_shopping(products)

    elif cmd=="list":
        print("Produkti:")
        list_shopping(products)

    elif cmd=="total":
        total_shopping(products)

    elif cmd=="clear":
        clear_shopping(products)
        
    else:
        print("Nezināma komanda.")

if __name__=="__main__":
    shop()