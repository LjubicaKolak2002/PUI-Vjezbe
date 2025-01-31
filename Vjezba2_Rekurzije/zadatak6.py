
def is_zero(total, lst, combination=""):
    if len(lst) == 0:
        if total == 0:
            print(combination, "= 0")
            return True
        return False

    flag = False
    if is_zero(total + lst[0], lst[1:], combination + f" + {lst[0]}"):
        flag = True
    if is_zero(total - lst[0], lst[1:], combination + f" - {lst[0]}"):
        flag = True
    return flag 

def main():
    
    lst = [1, 4, 5, 2, 4]
    print(is_zero(0, lst))
    
if __name__ == '__main__':
    main()



