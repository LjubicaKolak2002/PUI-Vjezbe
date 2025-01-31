from random import randint
from igrac import Igrac
from briskula import Briskula

class Bot(Igrac):
    def __init__(self, ime):
        self.ime = ime
        
    def akcija(self, stanje_igre):
        briskula = stanje_igre["briskula"]
        ruka = stanje_igre["ruka"]
        stol = stanje_igre["stol"]
        
        if len(stanje_igre["stol"]) > 0:
            for karta_na_stolu in stol:
                for indeks, karta_u_ruci in enumerate(ruka):
                    if karta_u_ruci[1] == karta_na_stolu[1]:
                        if Briskula.bodovi.get(karta_u_ruci[0], 0) > Briskula.bodovi.get(karta_na_stolu[0], 0):
                            #print(Briskula.bodovi.get(karta_u_ruci[0], 0))
                            return indeks
                        
                    if karta_u_ruci[1] == briskula[1]:
                        return indeks
            
            for indeks, karta_u_ruci in enumerate(ruka):
                if karta_u_ruci[0] not in Briskula.bodovi:
                    return indeks
                        
            return randint(0, len(ruka) - 1) if ruka else -1
        
        if len(stanje_igre["stol"]) == 0:
            for indeks, karta_u_ruci in enumerate(ruka):
                if karta_u_ruci[0] not in Briskula.bodovi: 
                    return indeks 
                
            for indeks, karta_u_ruci in enumerate(ruka):
                if karta_u_ruci[1] == briskula[1] or karta_u_ruci[0] in Briskula.bodovi:
                    return indeks
            
            
            return randint(0, len(ruka) - 1) if ruka else -1
            
       
       

        
        
def main():
    stanje_igre = {
        "ruka": [(7, 'k'), (13, 's'), (1, 'b')],
        "briskula": (11, 's') ,
        "stol": []
    }
    bot = Bot("komp")
    print(bot.akcija(stanje_igre))
    
    
if __name__ == '__main__':
    main()