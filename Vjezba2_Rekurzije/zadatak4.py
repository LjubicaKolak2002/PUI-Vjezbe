
def merge(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])
    
                

def main():
    lst1 = [2, 4, 6, 8]
    lst2 = [1, 3, 5, 7, 9]
    print(merge(lst1, lst2))
if __name__ == '__main__':
    main()