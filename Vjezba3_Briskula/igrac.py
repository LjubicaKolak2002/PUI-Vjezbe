from random import randint

class Igrac:
    def __init__(self, ime):
        self.ime = ime
       
        
    def akcija(self, stanje_igre):
        ruka = stanje_igre["ruka"]
        if not ruka:
            return -1  
        return randint(0, len(ruka) - 1)


        
def main():
    stanje_igre = {
        "ruka": ["(1, k)", "(2, s)", "(3, b)"],
    }
    
    print("Ruka prije", stanje_igre["ruka"])
    igrac1 = Igrac("igrac1")
    print("\nBacena karta na ideksu: ", igrac1.akcija(stanje_igre))
    print("\nRuka poslije: ", stanje_igre["ruka"])
  
if __name__ == '__main__':
    main()
        
        
        