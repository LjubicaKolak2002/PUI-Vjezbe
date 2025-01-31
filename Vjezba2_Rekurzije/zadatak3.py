
def binary_search(lst, num, start, end):
    if end < start:
        return 'Element ne postoji u listi'
    
    if lst[(start + end) // 2] == num:
        return f'Element je u listi na poziciji {(start + end) // 2}'
    elif lst[(start + end) // 2] > num:
        return binary_search(lst, num, start, ((start + end) // 2) - 1)
    else:
        return binary_search(lst, num, ((start + end) // 2) + 1, end)
    

def main():
    lst = [1, 2, 13, 20, 25, 50]
    # [1, 2, 13] [20, 25, 50] 20
    result = binary_search(lst, 20, 0, len(lst) - 1)
    print(result) 
    
    
if __name__ == '__main__':
    main()
