from random import randint

computer_number = randint(0, 1000)
print("Slučajno generirani broj: ", computer_number)
    
while True:
    user_number = int(input("Pogodite broj: "))
    
    if computer_number < user_number:
        print(f"Generirani broj je manji od", user_number)
    elif computer_number > user_number:
        print(f"Generirani broj je veći od", user_number)
    else:
        print("Pogodak!")
        break