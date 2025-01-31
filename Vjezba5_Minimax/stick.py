class StickGame:
    def __init__(self, sticks_num=11, player="Human"):
        self.sticks_num = sticks_num
        self.player = player
        self.options = [1, 2]

    def __str__(self):
        return "Broj štapića: " + str(self.sticks_num) + "\nPobjednik: " + str(self.get_winner()) + "\nGubitnik: " + str(self.get_loser()) 

    def get_player(self):
        return self.player

    def get_options(self):
        return self.options

    def get_sticks(self):
        return self.sticks_num 
    
    def get_loser(self):
        return "Computer" if self.player == "Computer" else "Human" 
    
    def get_winner(self):
        return "Human" if self.player == "Computer" else "Computer" 

    def change_player(self):
        self.player = "Computer" if self.player == "Human" else "Human"

    def do(self, number):
        self.sticks_num -= number
        self.change_player()

    def undo(self, number):
        self.sticks_num += number
        self.change_player()

    def game_over(self):
        if self.sticks_num < 0:
            return self.player
        elif self.sticks_num == 0:
            return self.player
        elif self.sticks_num < 2:   
            return "Human" if self.player == "Computer" else "Computer" 
        
        return "play"
    
