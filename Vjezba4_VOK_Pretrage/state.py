from copy import deepcopy

class State:
    def __init__(self, description="VOKB | | ----"):
        self.description = description
        
    def __str__(self):
        return  "".join(self.description)
    
    def is_solved(self):
        return True if self.description == "---- | | VOKB" else False
    
    def is_terminal(self):
        if self.description[-1] == "B" and self.description[6] == " ":
            if ('VO' in self.description[:4]) and self.description != "VOK- | | ---B":
                return True
            if ('OK' in self.description[:4]) and self.description != "VOK- | | ---B":
                return True
        elif self.description[3] == "B" and self.description[6] == " ":
            if ('VO' in self.description[9:]):
                return True
            if ('OK' in self.description[9:]):
                return True
        else:
            return False
    
    def next_states(self):
        next_states = []
        
        for action in self.all_actions():
            new_state = self.copy()
            new_state.action(action)
            next_states.append(new_state)
        return next_states
    
    
    def all_actions(self):
        actions = []
        indexes = {}
        
        for i, char in enumerate(self.description):
            if char in 'VOKB':
                indexes[char] = i
                
        if self.description[6] == " ":
            for char in 'VOK':
                if char in indexes and indexes[char] < 4 and self.description[3] == 'B':
                    actions.append(f"ukrcaj {char}")
                elif char in indexes and indexes[char] >= 9 and self.description[-1] == 'B':
                    actions.append(f"ukrcaj {char}")
        elif self.description[6] != " ":
            for char in 'VOK':
                if self.description[6] == char and self.description[3] == 'B':
                    actions.append(f"iskrcaj {char}")
                elif self.description[6] == char and self.description[-1] == 'B':
                    actions.append(f"iskrcaj {char}")
        if self.description[6] == " ":
            actions.append("prebaci brod")
        return actions
            
        
    def move_object_right(self, obj):
        if obj == "V":
            self.description[-4] = obj
        elif obj == "O":
            self.description[-3] = obj
        elif obj == "K":
            self.description[-2] = obj
        self.description[6] = " "
        return self
            
    def move_object_left(self, obj):
        if obj == "V":
            self.description[0] = obj
        elif obj == "O":
            self.description[1] = obj
        elif obj == "K":
            self.description[2] = obj
        self.description[6] = " "
        return self
    
    def move_boat(self):
        if self.description[3] == "B":
            self.description[-1] = "B"
            self.description[3] = "-"
        else: 
            self.description[3] = "B"
            self.description[-1] = "-"
    
    
    def check_boat(self, obj):
        """ if self.description[6] != " ":
           self.move_object_right(self.description[6]) """
        self.description[self.description.index(obj)] = '-'
        self.description[6] = obj
       

    def action(self, action):
        self.description = list(self.description)
        action_name, obj = action.split()
    
        #print(action)
        if action_name == "ukrcaj":
            if obj in self.description and self.description[6] == " " :
                self.check_boat(obj)
                self.move_boat()
        elif action_name == "prebaci":
            self.move_boat()
        elif action_name == "iskrcaj":
            boat_index = self.description.index("B")
            if (boat_index == 12) and obj == self.description[6]:
                self.move_object_right(obj)
            elif (boat_index == 3) and obj == self.description[6]:
                self.move_object_left(obj)
                
        self.description = "".join(self.description)
        return self

    def copy(self):
        return deepcopy(self)
    
    def undo_action(self, action):
        self.description = list(self.description)
        action_name, obj = action.split()
        boat_index = self.description.index("B")
        
        if action_name == "ukrcaj":
            if (boat_index == 3):
                self.move_object_right(obj)
            else:
                self.move_object_left(obj)
            self.move_boat()
        if action_name == "iskrcaj":
            if (boat_index == 12):
                if obj == "V":
                    self.description[-4] = '-'
                elif obj == "O":
                    self.description[-3] = '-'
                    
                elif obj == "K":
                    self.description[-2] = '-'
            else: 
                if obj == "V":
                    self.description[0] = '-'
                elif obj == "O":
                    self.description[1] = '-'
                elif obj == "K":
                    self.description[2] = '-'
            self.description[6] = obj
        if action_name == "prebaci":
            self.move_boat()
            
        self.description = "".join(self.description)
        return self
    

def main():

    pocetno_stanje = State("-OK- |V| ---B")
    print(f"Pocetno stanje: {pocetno_stanje}")
    #print("is terminal ", pocetno_stanje.is_terminal())
    #print("\nSve akcije trenutnog stanja\n", pocetno_stanje.all_actions())
    
    #pocetno_stanje.action("ukrcaj V")
    #print("Stanje nakon ukrcaj V", pocetno_stanje)
    
    #pocetno_stanje = pocetno_stanje.undo_action("iskrcaj V")
    #print("Stanje nakon ponistenja posljednje akcije:", pocetno_stanje)
    
    #sljedeca_stanja = pocetno_stanje.next_states()
    pocetno_stanje.action("prebaci brod")
    print("STANJE PRIJE UNDO ", pocetno_stanje.description)
    pocetno_stanje.undo_action("prebaci brod")
    print("STANJE NAKOn UNDO ", pocetno_stanje.description)
    #lst = pocetno_stanje.all_actions()
    #for action in pocetno_stanje.all_actions():
        #pocetno_stanje.action(action)
        #print("pocetno ", pocetno_stanje.description)
    #print("\nSljedeca stanja:")
    #for i, stanje in enumerate(sljedeca_stanja, 1):
        #print(f"Stanje {i}: {stanje}")
    
    
        
        
if __name__ == "__main__":
    main()