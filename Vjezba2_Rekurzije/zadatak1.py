
def predikat(element):
    return True if element % 2 == 0 else False

def count_iter(lst, predikat):
    cnt = 0
    for element in lst:
        if predikat(element):
            cnt += 1
    return cnt

def count_rek(lst, predikat):
    if len(lst) == 0:
        return 0
    
    if predikat(lst[0]):
        return 1 + count_rek(lst[1:], predikat)
    else:
        return 0 + count_rek(lst[1:], predikat)
        

def main():
    lst = [2, 31, 13, 14, 9, 20, 25, 6]
    print('Rezultat iterativne:', count_iter(lst, predikat))
    print('Rezultat rekurzivne:', count_rek(lst, predikat))
    
if __name__ == '__main__':
    main()
