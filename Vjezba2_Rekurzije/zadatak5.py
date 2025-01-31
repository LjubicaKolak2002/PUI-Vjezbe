
def generate_lst(n, string = ""):
    if len(string) == n:
        return [ string ]
    
    return generate_lst(n, string + 'A') + generate_lst(n, string + 'B') + generate_lst(n, string + 'C')


def main():
    print(generate_lst(3))
    
if __name__ == '__main__':
    main()