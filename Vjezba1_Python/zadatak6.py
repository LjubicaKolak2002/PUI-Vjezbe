from random import randint

user_number = int(input("Unesite broj u intervalu [0, 1000>: "))
min, max = 0, 1000

while True:
    computer_number = randint(min, max)
    print("Racunalo: ", computer_number)
    
    if computer_number < user_number:
        print("Zamišljeni broj je veći")
        min = computer_number
    elif computer_number > user_number:
        print("Zamišljeni broj je manji")
        max = computer_number
    else:
        print("Pogodak!")
        break
    #print("Min:", min, "Max:", max)
    
