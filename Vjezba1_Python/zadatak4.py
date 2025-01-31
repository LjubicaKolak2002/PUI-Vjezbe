
def check(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    return True
    
number1 = int(input("Prvi broj: "))
number2 = int(input("Drugi broj: "))

lst1, lst2 = list(str(number1)), list(str(number2))

if check(lst1, lst2):
    if sorted(lst1) == sorted(lst2):
        print("Brojevi su sastavljeni od istih znamenaka")
    else:
        print("Brojevi nisu sastavljeni od istih znamenaka")
else:
    print("Brojevi nisu iste dužine")
