from stick import StickGame

cnt = 0
def minimax(game):
    global cnt
    cnt += 1
    
    if game.game_over() == "Human":
        return 100, 0  
    elif game.game_over() == "Computer":
        return -100, 0  
        
    if game.player == "Human":
        maxi, num = -1000, 0 
        for number in game.get_options():
            game.do(number)
            vmax, _ = minimax(game)
            game.undo(number)
            
            if vmax > maxi:
                maxi, num = vmax, number
                
        return maxi, num  
    else:
        mini, num = 1000, 0
        for number in game.get_options():
            game.do(number)
            vmin, _ = minimax(game)
            game.undo(number)
            
            if vmin < mini:
                mini, num = vmin, number
                
        return mini, num


def minimax_alpha_beta(game, alpha, beta):
    global cnt 
    cnt += 1
    if game.game_over() == "Human":
        return 100, 0  
    elif game.game_over() == "Computer":
        return -100, 0  
    
    if game.get_player() == "Human":
        best = -1000
        for number in game.get_options():
            game.do(number)
            vmax, _  = minimax_alpha_beta(game, alpha, beta)
            game.undo(number)
            
            if vmax > alpha:
                alpha = vmax
                best = number
            if alpha >= beta:
                return alpha, None
        return alpha, best
              
    else:
        best = 1000
        for number in game.get_options():
            game.do(number)
            vmin, _ = minimax_alpha_beta(game, alpha, beta)
            game.undo(number)
            
            if vmin < beta:
                beta = vmin
                best = number
            if alpha >= beta:
                return beta, None
        return beta, best
                
    
def play_game(game):
    while game.game_over() == "play":
        print("Broj štapića: ", game.get_sticks(), "\n")
        
        if game.player =="Human":
            m = int(input("Odaberite 1 ili 2 štapića: "))
            
            while m not in game.get_options():
                m = int(input("Odaberite 1 ili 2 štapića: "))
            
            
            print("Igrač odabire:",m)
            
        else:
            #_, m = minimax(game)
            _, m = minimax_alpha_beta(game, -1000, 1000)
           
          
            print("Računalo odabire:", m, "\n")
            
        game.do(m)
    print(game.__str__())

    
 
if __name__ == "__main__":
    game = StickGame()
    #play_game(game)
    
    #minimax(game)
    #print("Broj cvorova:", cnt)
    
    play_game(game)
    #minimax_alpha_beta(game, -1000, 1000)
    #print("Broj cvorova za alpha beta", cnt)