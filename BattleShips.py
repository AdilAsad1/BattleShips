import random

def create_board():                 
    board = []
    for i in range(0,10):
        board.append(["o"]*10)
    return board

def print_board(board):             
    for i in board:
        print(" ".join(i))


def hide_ships(board):              
    possible_locations = []
    locations = []
  
    for i in range(0,len(board[0])):
        for j in range(0,len(board[0])):
            possible_locations.append([i,j])

    ship1_loc = random.randint(1,100)
    locations.append(possible_locations[ship1_loc])
    possible_locations.pop(ship1_loc)

    ship2_loc = random.randint(1,99)
    locations.append(possible_locations[ship2_loc])
    possible_locations.pop(ship2_loc)
    
    ship3_loc = random.randint(1,98)
    locations.append(possible_locations[ship3_loc])
    possible_locations.pop(ship3_loc)

    return locations

def print_rules():                      
    print("This is a 1 player game")
    print("You have 10 guesses to find and sink 3 ships hidden at random locations in the grid")
    print("Each time you guess correctly, you will get 3 extra guesses")
    print("Goodluck!")


def guess_check(guess,locations):   
    for i in locations:
        if guess == i:
            locations.remove(i)
            return 1
        else:
            return 0


def one_player():               
    player_name = input('Enter your name: ')
    print('Hi!',player_name)
    print_rules()
    board = create_board()
    print_board(board)
    locations = hide_ships(board)
    #print(locations)

    guess = 10
    hit_count = 0

    while guess != 0 and hit_count != 3:
        print('You have ',guess,'guesses')
        guess_row = int(input("Guess Row: (allowed values: 0-9) "))
        guess_col = int(input("Guess Col: (allowed values: 0-9) "))
        if (guess_row < 0 or guess_row > 9)  or (guess_col < 0 or guess_col > 9):
            print('Incorect values entered please only enter allowed values')
            continue
        else:
            gus = [guess_row,guess_col]
            check = guess_check(gus,locations)

            if check == 1:
                print('Congratulations! you sunk a ship!')
                hit_count += 1
                print('Only ', 3 - hit_count, 'ships remaining!')
                board[guess_row][guess_col] = "X"
                print_board(board)
                guess += 3
                

            elif check == 0:
                print('You missed!')
                print_board(board)
                guess -= 1
        
        
    if hit_count != 3 and guess == 0:
        print('You\'re all out of guesses!')
        print('Game Over!')
        print('You lost!')

    elif hit_count == 3:
        print('You won!!!')


def two_player():               
    player1_name = input("Enter player 1 name: ")
    player2_name = input("Enter player 2 name: ")
    print('Hi!',player1_name,'and',player2_name)
    board = create_board()
    print_board(board)
    player1_loc = []
    player2_loc = []
    print(player1_name," please enter the locations for your ships")
    for i in range(3):
        loc_row = int(input("Guess Row: (allowed values: 0-9) "))
        loc_col = int(input("Guess Col: (allowed values: 0-9) "))
        player1_loc.append([loc_row,loc_col])

    
    print(player2_name," please enter the locations for your ships")
    for i in range(3):
        loc_row = int(input("Guess Row: (allowed values: 0-9) "))
        loc_col = int(input("Guess Col: (allowed values: 0-9) "))
        player2_loc.append([loc_row,loc_col])

    player1_hits = 0
    player2_hits = 0

    while player1_hits != 3 or player2_hits != 3:
        print("It's",player1_name,"turn to guess!")
        guess_row = int(input("Guess Row: (allowed values: 0-9) "))
        guess_col = int(input("Guess Col: (allowed values: 0-9) "))
        
        gus = [guess_row,guess_col]
        check = guess_check(gus,player2_loc)

        if check == 1:
            print('Congratulations! you sunk a ship!')
            player1_hits += 1
            print('Only ', 3 - player1_hits, 'ships remaining!')
            board[guess_row][guess_col] = "X"
            print_board(board)
                

        elif check == 0:
            print('You missed!')
            print_board(board)
            
        print("It's",player2_name,"turn to guess!")
        guess_row = int(input("Guess Row: (allowed values: 0-9) "))
        guess_col = int(input("Guess Col: (allowed values: 0-9) "))
        
        gus = [guess_row,guess_col]
        check = guess_check(gus,player1_loc)

        if check == 1:
            print('Congratulations! you sunk a ship!')
            player2_hits += 1
            print('Only ', 3 - player2_hits, 'ships remaining!')
            board[guess_row][guess_col] = "X"
            print_board(board)
                

        elif check == 0:
            print('You missed!')
            print_board(board)


    if player1_hits == 3:
        print(player1_name," won!!!")

    elif player2_hits == 3:
        print(player2_name," won!!!")

        
    
    
    

def main():             
    print('Hello!')
    print('Welcome to battle ships')

    instr = input("One Player or Two player? enter 1 or 2 ")

    if instr == '1':
        one_player()
    elif instr == '2':
        two_player()
    

    while True:
        again = input('Would you like to play again? y/n: ')

        if again.lower() == 'y':
            main()
        elif again.lower() == 'n':
            print('Good Bye')
            exit()
        else:
            print('Invalid input')



main()
        
