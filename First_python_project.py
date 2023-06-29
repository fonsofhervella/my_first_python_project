#Creation of the game for human behavior prediction.

from mypackage.demo import linear_congruence
from mypackage.demo import player_propensities
from mypackage.demo import intelligent_machine
from mypackage.demo import print_scores

def correct_data_entry_errors (player_move):
    while True:
        try:
            player_move = int(input("Choose your move number %s (0 or 1): " % (turn+1)))
        except ValueError:
            print ("Please, enter a valid value")
            continue
        if player_move in (0,1):
            return player_move
            break
        else:
            print ("Please, enter a valid value")

print ('Welcome to Human Behaviour Prediction, a revolutionary game by Alfonso Ferrándiz Hervella')

while True:
    while True:
        try:
            select_difficulty = int(input("Choose your path (1 : Easy; 2 : Difficult): ")) 
        except ValueError:
            print ("Please, enter a valid value")
            continue
        if select_difficulty in (1, 2):
            break
        else:
            print ("Please, enter a valid value")
            
    moves = int(input("Enter the number of moves: "))
            
    MS = 0 #computerscore
    PS = 0 #playerscore
    xi = 1234 #seed
    player_move = None
    previous_move = None
    throw00 = 0 #num times player have chosen 0 after choosing 0
    throw10 = 0 #num times player have chosen 1 after choosing 0
    throw11 = 0 #num times player have chosen 1 after choosing 1
    throw01 = 0 #num times player have chosen 0 after choosing 1
    
    if select_difficulty == 1:
        for turn in range(moves):
            computer_move,xi = linear_congruence(xi)
            player_move = correct_data_entry_errors(player_move)
            PS, MS = print_scores(player_move, computer_move, PS, MS)
            print('PLAYER: ' + '*' *PS)
            print('COMPUTER: ' + '*' *MS)
    
    elif select_difficulty == 2:
        for turn in range(moves):
            if turn == 0 or turn ==1:
                computer_move,xi = linear_congruence(xi)
                player_move = correct_data_entry_errors(player_move)
                PS, MS = print_scores(player_move, computer_move, PS, MS)           
            else:
                computer_move, xi = intelligent_machine (throw00, throw01, throw10, throw11, xi)
                player_move = correct_data_entry_errors(player_move)
                PS, MS = print_scores(player_move, computer_move, PS, MS)
    
            throw00, throw01, throw10, throw11 = player_propensities (player_move, previous_move, throw00, throw01, throw10, throw11)
            previous_move = player_move
            
            print('PLAYER: ' + '*' *PS)
            print('COMPUTER: ' + '*' *MS)
     #Printing of the final results       
    if PS > MS: 
        print ("You win")
    elif PS < MS:
        print ("You loose")
    else:
        print ("It's a tie")    
    #Option to restart the game
    try:
        newgame = int(input("Do you want to start a new game (1 : Yes; 2 : No)? ")) 
    except ValueError:
        print ("Hope to see you soon!")
        break
    if newgame == 1:
        continue
    else:
        print ("Hope to see you soon!")
        break
    
