from igrac import Igrac

class Human(Igrac):
    def __init__(self, ime):
        self.ime = ime
        
    def akcija(self, stanje_igre):
        indeks_karte = int(input("Unesite indeks karte koju želite baciti (0-2): "))
        
        while (indeks_karte > len(stanje_igre["ruka"]) or indeks_karte < 0):
            indeks_karte = int(input("Unesite ponovno indeks karte: "))
        return indeks_karte  

def main():
    stanje_igre = {
        "ruka": ["(1, k)", "(2, s)", "(3, b)"],
    }
    
    human = Human("Human")
    indeks_karte = human.akcija(stanje_igre)
    odabrana_karta = stanje_igre["ruka"].pop(indeks_karte)  
    print("Odabrana karta:", odabrana_karta)
    print("Stanje ruke:", stanje_igre["ruka"])

    
if __name__ == '__main__':
    main()
