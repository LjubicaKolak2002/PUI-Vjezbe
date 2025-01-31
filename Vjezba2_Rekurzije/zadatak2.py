
# sa listom
def check_digits(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return True
    
    if lst1[0] in lst2:
        lst2.remove(lst1[0])
        lst1.pop(0)
        return check_digits(lst1, lst2)
    else:
        return False
    
# bez pretvaranja
def check_digit(digit, num):
    if num == 0:
        return False
    
    if num % 10 == digit:
        return True
    return check_digit(digit, num // 10)
    
    
def compare_numbers(num1, num2):
    if num1 == 0:
        return True
    
    if check_digit(num1 % 10, num2):
        return compare_numbers(num1 // 10, num2)
    return False
   
   

def main():
    num1 = int(input('Prvi broj: '))
    num2 = int(input('Drugi broj: '))
    
    lst1, lst2 =  list(str(num1)), list(str(num2))
    if check_digits(lst1, lst2):
        print('Brojevi imaju iste znamenke')
    else:
        print('Brojevi nemaju iste znamenke') 
    
    if compare_numbers(num1, num2):
        print('Brojevi imaju iste znamenke')
    else:
        print('Brojevi nemaju iste znamenke')
    
if __name__ == '__main__':
    main()
    