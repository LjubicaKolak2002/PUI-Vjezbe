from briskula import Briskula
from igrac import Igrac
from bot import Bot

def main():
    igrac1 = Igrac("igrac1")
    igrac2 = Bot("igrac2")
    briskula = Briskula(igrac1, igrac2)
    
    i, n = 0, 1000
    cnt0, cnt1, cnt2 = 0, 0, 0
    
    while i < n // 2:
        briskula = Briskula(igrac1, igrac2)
        briskula.odigraj_partiju(False)
        i += 1
        rezultat_partije = briskula.rezultat()
        if rezultat_partije == 0:
            cnt0 += 1
        elif rezultat_partije == 1:
            cnt1 += 1
        else:
            cnt2 += 1
        
    #print(igrac1.ime, ":", cnt1, igrac2.ime, ":", cnt2, "Nerijeseno:", cnt0) 
        
    i, cnt00, cnt01, cnt02 = 0, 0, 0, 0
    
    while i < n // 2:
        briskula2 = Briskula(igrac2, igrac1)
        briskula2.odigraj_partiju(False)
        i += 1
        rezultat_partije = briskula2.rezultat()
        if rezultat_partije == 0:
            cnt00 += 1
        elif rezultat_partije == 1:
            cnt02 += 1
        else:
            cnt01 += 1 
        
    #print(igrac1.ime, ":", cnt01, igrac2.ime, ":", cnt02, "Nerijeseno:", cnt00) 
    print("\nKONAČAN REZULTAT\n") 
    print(igrac1.ime, ":", cnt1 + cnt01, igrac2.ime, ":", cnt2 + cnt02, "Nerijeseno:", cnt0 + cnt00)
    
if __name__ == '__main__':
    main()
