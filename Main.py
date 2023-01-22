# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    #===================================================================================================================
    #HANAA ZAQOUT
    #HOMEWORK3
    #===================================================================================================================
    # file = open("input5.txt", "r")
    # ==================================================================================================================
    # REQUIRED DATA

    # Ships Data
    ships = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
    # Players Data
    players = {1:
                   {"available_ships": ["carrier", "battleship", "cruiser", "submarine", "destroyer"],
                    "position": [["-" for x in range(10)] for y in range(10)],
                    "hit": 0
                    },
               2:
                   {"available_ships": ["carrier", "battleship", "cruiser", "submarine", "destroyer"],
                    "position": [["-" for x in range(10)] for y in range(10)],
                    "hit": 0
                    },

               "default":
                   {"available_ships": ["carrier", "battleship", "cruiser", "submarine", "destroyer"],
                    "position": {1: [["-" for x in range(10)] for y in range(10)],
                                 2: [["-" for x in range(10)] for y in range(10)]}
                    }
               }

    # ===================================================================================================================
    # FIRST PHASE: PLACEMENT PHASE

    # default start with the first player
    player = 1
    # will be visible on the screen
    visible_lst = [players[player]["position"], players["default"]["position"][1]]

    # until players place all their shapes
    while players[player]["available_ships"] != []:

        # print the board on the screen
        print_3d_list(visible_lst)
        print_ships_to_be_placed()
        # show avaliable options
        for ship in players[player]["available_ships"]:
            print_single_element(ship[0].upper() + ship[1:])

        print_empty_line()
        print_player_turn_to_place(player)
        print_to_place_ships()

        # read input from text file
        # locate = file.readline().strip().split(" ")

        # recieve input from the user about ship's location
        locate = input().split(" ")

        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        # CATCH ERRORS IN THE GIVEN INPUT
        # if you catch any error in the input skip the current loop and start again asking for a new input

        # incorrect format if the given arguments are not enough OR x,y are not int
        if len(locate) < 4 or locate[1].isdecimal() == False or locate[2].isdecimal() == False:
            # call function that print the error on the screen
            print_incorrect_input_format()
            # skip to the next loop
            continue
            # will not run anything under this line, in this while loop

        # assign variables #
        name = locate[0].lower()
        x = int(locate[1]) - 1
        y = int(locate[2]) - 1
        orientation = locate[3].lower()

        # continue catching errors#

        if x > 9 or x < 0 or y > 9 or y < 0:
            print_incorrect_coordinates()
            continue
        if name not in players["default"]["available_ships"]:
            print_incorrect_ship_name()
            continue
        if orientation not in ["h", "v"]:
            print_incorrect_orientation()
            continue
        if name not in players[player]["available_ships"]:
            print_ship_is_already_placed(name[0].upper() + name[1:])
            continue
        if (orientation == "h" and x + ships[name] - 1 > 9) or (orientation == "v" and y + ships[name] - 1 > 9):
            print_ship_cannot_be_placed_outside(name[0].upper() + name[1:])
            continue
        if (orientation == "h") and (
                players[player]["position"][y][x:x + ships[name]] != ["-" for dash in range(ships[name])]):
            print_ship_cannot_be_placed_occupied(name[0].upper() + name[1:])
            continue
        if orientation == "v":
            empty = [False for point in range(y, y + ships[name]) if players[player]["position"][point][x] != "-"]
            # if there is any place occupied
            if False in empty:
                print_ship_cannot_be_placed_occupied(name[0].upper() + name[1:])
                continue

        # AWESOME as you reached here the input is Valid, Congratulations!!
        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        # DRAW THE SHIP ON THE BOARD

        if orientation == "h":
            players[player]["position"][y][x:x + ships[name]] = ["#" for dash in range(ships[name])]
            players[player]["available_ships"].remove(name)

        elif orientation == "v":
            for dash in range(y, y + ships[name]):
                players[player]["position"][dash][x] = "#"
            players[player]["available_ships"].remove(name)

        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        # CONFIRMATION STEP

        if players[player]["available_ships"] == []:
            print_3d_list(visible_lst)

            while True:
                print_confirm_placement()
                # answer = file.readline().strip().lower()
                answer = input().strip().lower()
                if answer == "y":
                    # switch to 2nd player
                    if player == 1:
                        player = 2
                        # 2nd player can not see 1st player board
                        visible_lst = [players["default"]["position"][1], players[player]["position"]]
                    break  # end of the FIRST PHASE

                if answer == "n":
                    # back to the default situation from scratch
                    players[player]["available_ships"] = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
                    players[player]["position"] = [["-" for x in range(10)] for y in range(10)]
                    # 1st player can not see 2nd player board
                    if player == 1:
                        visible_lst = [players[player]["position"], players["default"]["position"][1]]
                    # 2nd player can not see 1st player board
                    elif player == 2:
                        visible_lst = [players["default"]["position"][1], players[player]["position"]]
                    break

    # ===================================================================================================================
    # SECOND PHASE: BATTLE PHASE

    player = 1
    enemy = 2
    # will not stop till there is a player hit the 17 target
    while players[player]["hit"] != 17:

        # determine what is visiable
        if player == 1:
            visible_lst = [players[player]["position"], players["default"]["position"][2]]
        elif player == 2:
            visible_lst = [players["default"]["position"][1], players[player]["position"]]
        print_3d_list(visible_lst)
        print_player_turn_to_strike(player)
        print_choose_target_coordinates()
        # target = file.readline().strip().split(" ")
        target = input().strip().split(" ")

        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        # CATCH ERRORS IN THE GIVEN INPUT
        # the same logic used in the previous phase

        if len(target) < 2 or target[0].isdecimal() == False or target[1].isdecimal() == False:
            print_incorrect_input_format()
            continue

        # assign variables#
        x = int(target[0]) - 1
        y = int(target[1]) - 1

        # continue catching errors#
        if x > 9 or x < 0 or y > 9 or y < 0:
            print_incorrect_coordinates()
            continue

        # O means already struck but missed, ! means already struck and hit
        if players[enemy]["position"][y][x] in ["O", "!"]:
            print_tile_already_struck()
            continue

        # AWESOME as you reached here the input is Valid, Congratulations!!
        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
        # HIT THE TARGET

        # no ship => wrong target
        if players[enemy]["position"][y][x] == "-":
            # change the data of the enemy
            players[enemy]["position"][y][x] = "O"
            # stricks are visible to both players
            players["default"]["position"][enemy][y][x] = "O"
            print_miss()

            # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
            # DONE

            # because wrong target, this player turn is DONE
            while True:
                print_type_done_to_yield(enemy)
                # done_answer=file.readline().strip().lower()
                done_answer = input().strip().lower()
                if done_answer == "done":
                    # switch players
                    if player == 1:
                        player = 2
                        enemy = 1
                    elif player == 2:
                        player = 1
                        enemy = 2
                    break
                    # the loop will continue till the user enter the right input: done
        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

        # there is a ship => Right target
        elif players[enemy]["position"][y][x] == "#":
            # change enemy data
            players[enemy]["position"][y][x] = "!"
            # stricks are visible for everyone
            players["default"]["position"][enemy][y][x] = "!"
            print_hit()
            # plus to the player :D
            players[player]["hit"] += 1

        # BATTLE IS OVER
        # ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
    # PRINT THE LAST BOARD IN THE GAME

    if player == 1:
        visible_lst = [players[player]["position"], players["default"]["position"][2]]
    elif player == 2:
        visible_lst = [players["default"]["position"][1], players[player]["position"]]
    print_3d_list(visible_lst)

    # ===================================================================================================================
    # ANNOUNCING THE RESULT

    print_player_won(player)
    print_thanks_for_playing()

    # ===================================================================================================================
    # HOPE YOU ENJOYED THE GAME!!!
    # PLAY ONE MORE TIME
    # file.close()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()
