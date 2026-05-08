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