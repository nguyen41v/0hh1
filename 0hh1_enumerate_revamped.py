import time, random

#default settings
DEFAULT_TIME = "yes"
DEFAULT_HINTS = "yes"
show_time = "yes"
show_hints = "yes"
NO_SETTING = "no"
YES_SETTING = "yes"
#default tiles
TILE1 = "x"
TILE2 = "o"
EMPTY_TILE = " "
TILE1TEXT = "an " + TILE1
TILE2TEXT = "an " + TILE2
STARTING_TILE1 = TILE1.upper()
STARTING_TILE2 = TILE2.upper()

def opening_screen():
    print("\n\n\n0h h1\na little logic game\nby Q42\nrewritten by Vanessa Nguyen :3\n")
    input("Press enter to begin:\n---------------\n")


def start_page():
    print("\nOh hi\nThis is the menu\n---------------")
    print("1 - How to play\n2 - Play\n3 - Settings\n4 - About\n5 - Exit the game")
    start_page_action = input("---------------\nPlease type in the number corresponding to the action you wish to take:\n")

    #if their input wasn't a number corresponding to an action, make them input till it's valid
    valid = False
    if (start_page_action == "1") or (start_page_action == "2") or (start_page_action == "3") or (start_page_action == "4") or (start_page_action == "5"):
            valid = True
    while not valid:
        start_page_action = input("Your input was invalid. Please type in the number corresponding to the action you wish to take:\n")
        if (start_page_action == "1") or (start_page_action == "2") or (start_page_action == "3") or (start_page_action == "4") or (start_page_action == "5"):
            valid = True
    start_page_action = int(start_page_action)
    return start_action(start_page_action)


def start_action(start_page_action):
    if start_page_action == 1:
        how_to_play()
    if start_page_action == 2:
        play()
    if start_page_action == 3:
        settings()
    if start_page_action == 4:
        about()
    if start_page_action == 5:
        print("Thank you for playing!")


def how_to_play():
    #initial board
    size = 4
    playing_board = tutorial_board(empty_board(size))


    #how to put in x tiles; 1
    print("Capitalization matters in this game.\n"
          "Type in \q anytime you want to return to the menu.\n"
          "Type in \w to view the about page.\n")
    location = ""
    tile = ""

    while location != "A1":
        tutorial_board_draw_1(size, playing_board)
        location = input("We're going to fill the grid.\n"
                         "Type in the location of the outlined box (Ex. A1).\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE1:
        tile = input("Type in " + TILE1 + " to put " + TILE1TEXT + " tile here:\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    # next move, how to put in o tile; 2
    print("Excellent!")
    print("Don't forget that capitalization matters in this game.")
    location = ""
    tile = ""

    while location != "B1":
        tutorial_board_draw_2(size, playing_board)
        location = input("We're going to fill the grid with a different kind of tile.\n"
                         "Type in the location of the outlined box (Ex. B1).\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE2:
        tile = input("We're going to fill the grid with a different kind of tile.\n"
                     "Type in " + TILE2 + " to put " + TILE2TEXT + " tile here:\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #next move, three tiles of the same in a row isn't allowed, x; 3
    location = ""
    tile = ""
    while location != "A3":
        tutorial_board_draw_3(size, playing_board)
        location = input("Three " + TILE1 + " tiles next to each other in a row isn't allowed.\n"
                         "Type in the location of the outlined box (Ex. A3).\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE2:

        tile = input("Three " + TILE1 + " tiles next to each other in a row isn't allowed.\n"
                     "Which tile would you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #next move, three tiles of the same in a row isn't allowed, o; 4
    tutorial_board_draw_4(size, playing_board)
    location = ""
    tile = ""
    while location != "B2":
        location = input("Three " + TILE2 + " tiles next to each other in a row isn't allowed.\n"
                         "Type in the location of the outlined box (Ex. B2).\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE1:
        tile = input("Three " + TILE2 + " tiles next to each other in a row isn't allowed.\n"
                     "Which tile would you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #next move, three tiles of the same in a column isn't allowed, x/o; 5
    while playing_board[2][1] != TILE2 or playing_board[2][2] != TILE1:
        location = ""
        tile = ""
        while location != "C2" and location != "C3":
            tutorial_board_draw_5(size, playing_board)
            location = input("Three " + TILE1 + " or " + TILE2 + " tiles below each other is invalid too!\n"
                             "Type in the location of an outlined box(Ex. C2).\n")
            if location == "\q":
                start_page()
            if location == "\w":
                about()
        while tile != TILE1 and tile != TILE2:
            tile = input("Three " + TILE1 + " or " + TILE2 + " tiles below each other is invalid too!\n"
                         "Which tile would you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
            if tile == "\q":
                start_page()
            if tile == "\w":
                about()
        playing_board = action(playing_board, location, tile, size)


    #next move, row must have same x as o; 6
    location = ""
    tile = ""
    while location != "B4":
        tutorial_board_draw_6(size, playing_board)
        location = input("A full row must have as many " + TILE1 + " tiles as it has " + TILE2 + " ones.\n"
                         "Where would you like to place your next tile (Ex. B4)?\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE1:
        tile = input("A full row must have as many " + TILE1 + " tiles as it has " + TILE2 + " ones\n"
                     "Which tile would you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
        if tile == "\w":
            about()
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #next move, columns must have same x as o; 7
    location = ""
    tile = ""
    while location != "D2":
        tutorial_board_draw_7(size, playing_board)
        location = input("Columns have an equal number of each tile too.\n"
                         "Where would you like to place your next tile (Ex. D2)?\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE2:
        tile = input("Columns have an equal number of each tile too.\n"
                     "Which tile would you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #another column move; 8
    tutorial_board_draw_8(size, playing_board)
    location = ""
    tile = ""
    while location != "D3":
        location = input("You should be able to know what tile this one is...\n"
                         "Where would you like to place your next tile (Ex. D3)?\n")
        if location == "\q":
            start_page()
        if location == "\w":
            about()
    while tile != TILE1:
        tile = input("You should be able to know what tile this one is...\n"
                    "Which tile whould you like to place here  (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
        if tile == "\q":
            start_page()
        if tile == "\w":
            about()
    playing_board = action(playing_board, location, tile, size)


    #no two rows and no two columns same; 9
    location = ""
    tile = ""
    while playing_board[2][0] != TILE2 or playing_board[2][3] != TILE1 or playing_board[3][0] != TILE1:
        tutorial_board_draw_9(size, playing_board)
        while (location != "D1") and (location != "C1") and (location != "C4"):
            location = input("No two rows and no two columns are the same.\n"
                             "Where would you like to place your next tile (Ex. C1)?\n")
            if location == "\q":
                start_page()
            if location == "\w":
                about()
        while (tile != TILE1) and (tile != TILE2):
            tile = input("No two rows and no two columns are the same.\n"
                         "Which tile whould you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
            if tile == "\q":
                start_page()
            if tile == "\w":
                about()
        playing_board = action(playing_board, location, tile, size)


    #last tile, hint button; 10
    print("If you get stuck, type in \h to peek.")
    location = ""
    tile = ""
    while playing_board[0][3] != TILE2:
        tutorial_board_draw_10(size, playing_board)
        while location != "A4":
            location = input("If you get stuck, type in \h to peek.\n"
                             "Where would you like to place your next tile (Ex. A4)?\n")
            if location == "\q":
                start_page()
            if location == "\w":
                about()
            if location == "\h":
                show_hint(playing_board)
        while (tile != TILE1) and (tile != TILE2):
            tile = input("If you get stuck, type in \h to peek.\n"
                         "Which tile whould you like to place here (" + TILE1 + ", " + TILE2 + ", or ' ')?\n")
            if tile == "\q":
                start_page()
            if tile == "\h":
                show_hint(playing_board)
        playing_board = action(playing_board, location, tile, size)
    draw_board(size, playing_board)
    completion_message()
    play()


def tutorial_board(board):
    board[0][1] = STARTING_TILE1
    board[1][2] = STARTING_TILE2
    board[3][3] = STARTING_TILE2
    return board

#########################################################################
#START____ALL FOR EACH PART OF TUTORIAL ___##############################
def tutorial_board_draw_1(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if row == -1:
                print(" +====" + ("----" * (row_length - 1) + "---+"))
            elif row == 1:
                print(" =====" + ("----" * row_length))
            elif row == (total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "||" + board_list[board_row][0] + "|| "
                for inside_columns in range(1, row_length):
                    print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_2(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == 1) or (row == 3):
                print(" =====" + ("----" * row_length))
            elif (row == -1) or (row == total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 2:
                board_row = row // 2
                print_row = chr(board_row + 65) + "||" + board_list[board_row][0] + "|| "
                for inside_columns in range(1, row_length):
                    print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_3(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if row == -1:
                print(" +----" + "---" + "=====" + "---+")
            elif row == 1:
                print(" -----" + "---" + "====" + "----")
            elif row == (total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif row % 2 == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0] + " | "
                for inside_columns in range(1, row_length):
                    if inside_columns < 2:
                        print_row += board_list[board_row][inside_columns] + " ||"
                    elif inside_columns == 2:
                        print_row += board_list[board_row][inside_columns] + "|| "
                    else:
                        print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif row % 2 == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_4(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == 1) or (row == 3):
                print(" ----" + "=====" + ("----" * (row_length-1)))
            elif (row == -1) or (row == total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 2:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0] + " ||"
                for inside_columns in range(1, row_length):
                    if inside_columns == 1:
                        print_row += board_list[board_row][inside_columns] + "|| "
                    else:
                        print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_5(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == -1) or (row == total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row == 3) or (row == 5):
                print(" ----" + "=====" + "====" + "----")
            elif row % 2 == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 4:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0] + " ||"
                for inside_columns in range(1, row_length):
                    if inside_columns < 2:
                        print_row += board_list[board_row][inside_columns] + "|||"
                    elif inside_columns == 2:
                        print_row += board_list[board_row][inside_columns] + "|| "
                    else:
                        print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif row % 2 == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_6(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == 1) or (row == 3):
                print(" =====" + ("====" * row_length))
            elif (row == -1) or (row == total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 2:
                board_row = row // 2
                print_row = chr(board_row + 65) + "||" + board_list[board_row][0] + "|||"
                for inside_columns in range(1, row_length):
                    print_row += board_list[board_row][inside_columns] + "|||"
                print_row += board_list[board_row][row_length] + "||" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_7(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == -1) or (row == total_rows - 1):
                print(" +" + "---" + "=====" + "----" + "---+")
            elif (row % 2) == 1:
                print(" -" + "---" + "=====" + "----" * 2)

            #couting the rows from greatest to least to match board numbering set up
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0] + " ||" + board_list[board_row][1] + "|| "
                for inside_columns in range(2, row_length):
                    print_row += board_list[board_row][inside_columns] + " | "
                print_row += board_list[board_row][row_length] + "||" + chr(board_row + 65)
                print(print_row)
    print(num_row)


def tutorial_board_draw_8(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if row == total_rows - 1:
                print(" +" + ("----" * (row_length - 2) + "---" + "=====" + "---+"))
            elif row == total_rows - 3:
                print(" -" + ("----" * (row_length - 2)) + "---" + "=====" + "----")
            elif row == 1:
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 6:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0] + " | "
                for inside_columns in range(1, row_length):
                    if inside_columns == 2:
                        print_row += board_list[board_row][inside_columns] + "|| "
                    else:
                        print_row += board_list[board_row][inside_columns] + " ||"
                print_row += board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_9(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if row == total_rows - 1:
                print(" +" + ("===="*row_length) + "===+")
            elif (row == total_rows - 3) or (row == total_rows - 5):
                print(" =" + ("====" * size))
            elif row == 1:
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif (row == 4) or (row == 6):
                board_row = row // 2
                print_row = chr(board_row + 65) + "||" + board_list[board_row][0] + "|||"
                for inside_columns in range(1, row_length):
                        print_row += board_list[board_row][inside_columns] + "|||"
                print_row += board_list[board_row][row_length] + "||" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)


def tutorial_board_draw_10(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if row == -1:
                print(" +" + ("----" * (row_length) + "====+"))
            elif row == 1:
                print(" " + ("----" * row_length) + "=====")
            elif row == (total_rows - 1):
                print(" +" + ("----" * row_length) + "---+")
            elif (row % 2) == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " ||" + board_list[board_row][row_length] + "||" + chr(board_row + 65)
                print(print_row)
            elif (row % 2) == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)

    print(num_row)

#END____ALL FOR EACH PART OF TUTORIAL ___################################
#########################################################################

def play():
    size = input("Select a size:\n4\n6\n8\n10\n12\n...\nOr type in \q to return to the main menu.\n")

    #making sure the number they put in corresponds to a working game
    valid = 0
    if (size == "4") or (size == "6") or (size == "8") or (size == "10") or (size == "12") or (size == "...") or (size == "\q"):
        valid = 1
    while not valid:
        size = input("The size you selected was not valid. Please try again:\n")
        if (size == "4") or (size == "6") or (size == "8") or (size == "10") or (size == "12") or (size == "...")or (size == "\q"):
            valid = 1

    #go to game or other games screen
    if (size != "...") and (size != "\q"):
        play_board(int(size))
    if size == "...":
        other_games()
        input("\nClick enter to go back to board size selection:\n")
    if size == "\q":
        start_page()
    else:
        play()


def play_board(size):
    finished_board = complete_board(size, empty_board(size))
    draw_board(size, finished_board)
    playing_board = starting_board(size, finished_board)
    start_time = time.time()
    incomplete_game = True
    print("Type in \q to quit the game anytime.\nType in \h for hints.\nType in \w to view the about page.")
    while incomplete_game:
        draw_board(size, playing_board)
        if show_time == "yes":
            time_at = time.time() - start_time
            print("Time spent on current game: " + str(round(time_at, 2)) + " seconds")
        move = make_move(size, playing_board)
        if move == "\q":
            return
        tile = placing(size, playing_board)
        if tile == "\q":
            return
        playing_board = action(playing_board, move, tile, size)
        if board_full(playing_board, size):
            incomplete_game = incomplete(playing_board)
            if incomplete_game:
                if show_hints == "yes":
                    show_hint(size, playing_board)
    draw_board(size, playing_board)
    completion_message()
    if show_time == "yes":
        time_taken = time.time() - start_time
        print("You've spent " + str(round(time_taken, 2)) + " seconds total on this game.")


def empty_board(size):
    """reference_board =
                      [[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12],
                       [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12],
                       [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12],
                       [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12],
                       [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12],
                       [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12],
                       [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12],
                       [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12],
                       [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12],
                       [j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12],
                       [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12],
                       [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12]]
    """
    game_board = []
    for row in range(size):
        board_row = []
        for i in range(size):
            if i % 2 == 0:
                board_row += TILE1
            else:
                board_row += TILE2
        random.shuffle(board_row)
        game_board.append(board_row)
    return game_board


def complete_board(size, board_list):
    not_done = True
    while not_done:
        row = 0
        while row < size:
            column = 0
            while column < size:
                # makes sure row has same x and o
                if column % 2 == 0:
                    tile = STARTING_TILE1
                else:
                    tile = STARTING_TILE2
                board_list[row][column] = tile
                column += 1
            random.shuffle(board_list[row])

            #checking for rule breaks in pattern
            sad_life = True
            sad_life_squared = True
            while sad_life:
                while sad_life_squared:

                    if row >= (size - 3): #fixme
                        for comparing_row in range(size):
                            tile1counter = 0
                            tile2counter = 0
                            for comparing_column in range(row):
                                if board_list[comparing_column][comparing_row] == TILE1:
                                    tile1counter += 1
                                if board_list[comparing_column][comparing_row] == TILE2:
                                    tile2counter += 1
                            if tile1counter == size // 2:

                    #comparing new row to previous two to check for xxx/ooo in up/down
                    column3 = 0
                    while column3 < size:
                        if 1 < row:
                            #if last column, just random shuffle
                            if column3 == (size - 1):
                                if board_list[row][column3] == board_list[row - 1][column3] == board_list[row - 2][column3]:
                                    for index, element in enumerate(board_list[row]):
                                        if index == (len(board_list[row]) - 1):
                                            random.shuffle(board_list[row])
                                            column3 = 0
                                            break
                                else:
                                    break
                            elif board_list[row][column3] == board_list[row - 1][column3] == board_list[row - 2][column3]:
                                #i read online that for: else: only does the else if the for (or while) loop wasn't broken through break
                                for index, element in enumerate(board_list[row][column3:]):
                                    if index == (len(board_list[row][column3:]) - 1):
                                        random.shuffle(board_list[row])
                                        column3 = 0
                                        break
                                    elif element != board_list[row][column3]:
                                        location = index + column3
                                        tile1 = board_list[row][column3]
                                        tile2 = board_list[row][location]
                                        board_list[row][column3] = tile2
                                        board_list[row][location] = tile1
                                else:
                                    column3 += 1
                            else:
                                column3 += 1
                        else:
                            break

                    #checking for xxx/ooo in a row
                    column4 = 0
                    while column4 < size - 2:
                        if board_list[row][column4] == board_list[row][column4 + 1] == board_list[row][column4 + 2]:
                            while board_list[row][column4] == board_list[row][column4 + 1] == board_list[row][column4 + 2]:
                                random.shuffle(board_list[row])
                            sad_life_squared = True
                            break
                        else:
                            column4 += 1
                            sad_life_squared = False

                # if row is the same as previous rows, redo row
                if row > 0:
                    row4 = 0
                    while row4 < row:
                        if board_list[row] == board_list[row4]:
                            random.shuffle(board_list[row])
                            sad_life_squared = True
                            break
                        else:
                            row4 += 1
                    if row4 == row:
                        sad_life = False
                else:
                    sad_life = False

            row += 1
        draw_board(size,board_list)
        #redos whole board if columns have xxx/ooo, are the same, or if columns don't have same x and o; row - 1 keeps row in range
        row -= 1
        row4 = 0
        row_to_col_list = []

        #redos whole board if columns have xxx/ooo
        for col in range(size):
            for row in range(2, size):
                if board_list[row][col] == board_list[row - 1][col] == board_list[row - 2][col]:
                    row4 = row + 1

        #converts col to row to make it easier to analyze
        for col in range(size):
            plus_to_list = []
            for row in range(size):
                plus_to_list += [board_list[row][col]]
            row_to_col_list += [plus_to_list]

        for column_now_row in row_to_col_list:
            sum_column = 0
            for tile in column_now_row:
                sum_column += ord(tile)
            if sum_column != ((ord(TILE1) + ord(TILE2)) * size // 2):
                row4 = row + 1
                break


        #redos whole board if columns are the same
        if row4 < row:
            for row in range(size):
                row4 = 0
                while row4 < row:
                    if row_to_col_list[row] == row_to_col_list[row4]:
                        random.shuffle(board_list[row])
                        row4 = row + 1
                        break
                    else:
                        row4 += 1
                else:
                    continue
                break
        if row4 == row:
            not_done = False


    return board_list
#hahahahaha


def starting_board(size, board_list):
    board_list[random.randint(0, size - 1)][random.randint(0, size - 1)] = EMPTY_TILE
    can_remove_tiles = 0
    random_row_list1 = []
    random_row_list2 = []
    for i in range(size):
        random_row_list1 += [i]
    for i in range(size - 2):
        random_row_list2 += [i]
    while can_remove_tiles < size ** 3:
        remove_number = random.randint(1,13)
        random.shuffle(random_row_list1)
        random.shuffle(random_row_list2)
        while can_remove_tiles < size ** 2:
            remove_number = random.randint(1, 13)
            random.shuffle(random_row_list1)
            random.shuffle(random_row_list2)
            # checks for complete/almost complete rows and removes tile
            if remove_number == 1 or remove_number == 2 or remove_number == 3 or remove_number == 4:
                row = random_row_list1[0]
                tile1counter = 0
                tile2counter = 0
                tile1index = []
                tile2index = []
                for column in board_list[row]:
                    if column == TILE1:
                        tile1counter += 1
                        tile1index += [row]
                    if column == TILE2:
                        tile2counter += 1
                        tile2index += [row]
                if remove_number == 1:
                    if (tile1counter == (size // 2)) and (tile2counter == (size // 2) - 1):
                        board_list[row][tile2index[0]] = EMPTY_TILE
                    elif (tile2counter == (size // 2)) and (tile1counter == (size // 2) - 1):
                        board_list[row][tile1index[0]] = EMPTY_TILE
                    elif tile1counter == (size // 2):
                        board_list[row][tile1index[0]] = EMPTY_TILE
                    elif tile2counter == (size // 2):
                        board_list[row][tile2index[0]] = EMPTY_TILE

                elif remove_number == 2:
                    if (tile2counter == (size // 2)) and (tile1counter >= (size // 2) - 1):
                        board_list[row][tile1index[0]] = EMPTY_TILE
                    elif (tile1counter == (size // 2)) and (tile2counter >= (size // 2) - 1):
                        board_list[row][tile2index[0]] = EMPTY_TILE
                    elif tile2counter == (size // 2):
                        board_list[row][tile2index[0]] = EMPTY_TILE
                    elif tile1counter == (size // 2):
                        board_list[row][tile1index[0]] = EMPTY_TILE

                elif remove_number == 3:
                    if tile1counter == (size // 2):
                        board_list[row][tile1index[0]] = EMPTY_TILE
                    elif tile2counter == (size // 2):
                        board_list[row][tile2index[0]] = EMPTY_TILE

                elif remove_number == 4:
                    if tile2counter == (size // 2):
                        board_list[row][tile2index[0]] = EMPTY_TILE
                    elif tile1counter == (size // 2):
                        board_list[row][tile1index[0]] = EMPTY_TILE


            #checks for complete/almost complete columns and removes a tile
            if remove_number == 4 or remove_number == 5 or remove_number == 6 or remove_number == 7:
                pass
            #checks for xx/oo in rows and removes x/o around them
            if remove_number == 8 or remove_number == 9:
                row = random_row_list1[0]
                column = random_row_list2[0]
                if board_list[row][column] == board_list[row][column + 1]:
                    if column == 0:
                        board_list[row][column + 2] = EMPTY_TILE
                    elif column == size - 2:
                        board_list[row][column - 1] = EMPTY_TILE
                    else:
                        if remove_number == 8:
                            board_list[row][column - 1] = EMPTY_TILE
                        else:
                            board_list[row][column + 2] = EMPTY_TILE


            if remove_number == 10 or remove_number == 11:
                pass

            #checks for x_x/o_o in rows and removes x/o in them
            if remove_number == 12 or remove_number == 13:
                row = random_row_list1[0]
                column = random_row_list2[0]
                if board_list[row][column] == board_list[row][column + 2]:
                        board_list[row][column + 1] = EMPTY_TILE
            can_remove_tiles += 1

        # checks for x_x/o_o in rows and removes x/o in them
        if remove_number > 6:
            for row in random_row_list1:
                for column in random_row_list2:
                    if board_list[row][column] == board_list[row][column + 2]:
                        board_list[row][column + 1] = EMPTY_TILE

        # checks for xx/oo in rows and removes x/o around them
        elif remove_number <= 6:
            for row in random_row_list1:
                for column in random_row_list2:
                    if board_list[row][column] == board_list[row][column + 1]:
                        if column == 0:
                            board_list[row][column + 2] = EMPTY_TILE
                            break
                        elif column == len(board_list[row]) - 1:
                            board_list[row][column - 1] = EMPTY_TILE
                            break
                        else:
                            if remove_number == 8:
                                board_list[row][column - 1] = EMPTY_TILE
                                break
                            else:
                                board_list[row][column + 2] = EMPTY_TILE
                                break
                else:
                    continue
                break
        can_remove_tiles += 1
    return board_list


def draw_board(size, board_list):
    total_rows = size * 2

    #for the indices i guess
    row_length = size - 1

    #number labeling on top/bot
    num = 0
    num_row = " "
    while num < size:
        num = num + 1
        if num <= 10:
            num_row += "  " + str(num) + " "
        else:
            num_row += " " + str(num) + " "
    print(num_row)

    for row in range(-1, total_rows):
            if (row == -1) or (row == total_rows-1):
                print(" +" + ("----" * row_length) + "---+")
            elif row % 2 == 1:
                print(" -" + ("----" * size))

            #couting the rows from greatest to least to match board numbering set up
            elif row % 2 == 0:
                board_row = row // 2
                print_row = chr(board_row + 65) + "| " + board_list[board_row][0]
                for inside_columns in range(1, row_length):
                    print_row += " | " + board_list[board_row][inside_columns]
                print_row += " | " + board_list[board_row][row_length] + " |" + chr(board_row + 65)
                print(print_row)
    print(num_row)


def make_move(size, board):
    location = ""
    possible_locations = grid(size)
    while (not (location in possible_locations.split(" "))) or location == "":
        location = input("Where would you like to place your next tile?\n")
        if location == "\q":
            return "\q"
        if location == "\w":
            about()
        if location == "\h":
            show_hint(size, board)
    return location


def grid(size):
    possible_locations = ""
    for num in range(size):
        for let in range(size):
            possible_locations += chr(let + 65) + str(num + 1) + " "
    return possible_locations


def placing(size, board):
    tile = ""
    while (tile != TILE1) and (tile != TILE2):
        tile = input("Which tile would you like to place here?\n")
        if tile == "\q":
            return "\q"
        if tile == "\w":
            about()
        if tile == "\h":
            show_hint(size, board)
    return tile


#replaces old tile with new tile
def action(board, location, tile, size):
    let = 65
    board_row = 0
    while let != ord(location[0]):
        let += 1
        board_row += 1
    num = 1
    board_column = 0
    while num != int(location[1:]):
        num += 1
        board_column += 1
    if board[board_row][board_column] == STARTING_TILE1 or board[board_row][board_column] == STARTING_TILE2:
        print("This tile is a locked tile. Please re-choose your location")
        return action(board, make_move(size, board), placing(size, board), size)
    if board[board_row][board_column] != " ":
        choice = input("This location already has a tile placed. "
                       "Type in 1 to re-choose your location, "
                       "else click enter if you'd like to replace this tile with your current tile:\n")
        if choice == 1:
            return action(board, make_move(size, board), placing(size, board), size)
    board[board_row][board_column] = tile
    return board


def show_hint(size, board):
    print("The hint feature has not been implemented yet. It will arrive soon™.")
    if board:
        return board
    return board


def completion_message():
    message = ["Wonderful!", "Spectacular!", "Marvelous!", "Outstanding!", "Remarkable!", "Shazam!",
               "Impressive!", "Great!", "Well done!", "Fabulous!", "Clever!", "Dazzling!", "Fantastic!",
               "Excellent!", "Nice!", "Super!", "Awesome!", "Ojoo!", "Brilliant!", "Splendid!",
               "Exceptional!", "Magnificent!", "Yay!"]
    random.shuffle(message)
    print(message[0])


def board_full(board, size):
    for row in range(size):
        for column in range(size):
            if board[row][column] == " ":
                return False
    return True


def incomplete(board):
    if board: #fixme
        return True
    else:
        return False


def settings():
    global show_time, show_hints
    want_settings_changed = "1"
    while want_settings_changed == "1":
        print("\nSettings\n---------------\nShow elapsed time - " + show_time + "\nShow hint icon - " + show_hints)
        want_settings_changed = input("Press 1 if you would like to change your settings, "
                                      "otherwise press enter to go back:\n")
        while (want_settings_changed != "1") and (want_settings_changed != ""):
            want_settings_changed = input("Your input was invalid. "
                                          "Press 1 if you would like to change your settings, "
                                          "otherwise press enter to go back:\n")
        if want_settings_changed == "1":

            #setting variables to = opposite of current settings
            if show_time != NO_SETTING:
                opposite_time_setting = NO_SETTING
            if show_time != YES_SETTING:
                opposite_time_setting = YES_SETTING
            if show_hints != NO_SETTING:
                opposite_hints_setting = NO_SETTING
            if show_time != YES_SETTING:
                opposite_hints_setting = YES_SETTING
            change_setting = input("Type in 1 to change the elapsed time setting to " + opposite_time_setting + ", "
                                   "2 to change the hint setting to " + opposite_hints_setting + ", "
                                   "3 to change both, "
                                   "4 to reset the settings to default, "
                                   "or enter to continue without changes:\n")
            if change_setting == "1":
                show_time = opposite_time_setting
                print("Your elapsed time setting has been changed to " + opposite_time_setting + ".")
            elif change_setting == "2":
                show_hints = opposite_hints_setting
                print(("Your hint setting has been changed to " + opposite_hints_setting + "."))
            elif change_setting == "3":
                show_time = opposite_time_setting
                show_hints = opposite_hints_setting
                print("Your elapsed time setting has been changed to " + opposite_time_setting +
                      " and your hint setting has been changed to " + opposite_hints_setting + ".")
            elif change_setting == "4":
                show_time = DEFAULT_TIME
                show_hints = DEFAULT_HINTS
                print("Your elapsed time setting has been changed to " + DEFAULT_TIME +
                      " and your hint setting has been changed to " + DEFAULT_HINTS + ".")
            else:
                print("No changes have been made")
    start_page()


def about():
    about_screen()
    input("\nClick enter to continue:\n")
    rules()
    input("\nClick enter to continue:\n")
    apps()
    input("\nClick enter to continue:\n")
    other_games()
    input("\nClick enter to go back:\n")
    start_page()


def about_screen():
    print("\nAbout"
          "\n---------------"
          "\n0h h1 is a little logic game"
          "\nby Q42. It was created by"
          "\nMartin Kool."
          "\n\nThe concept is also known"
          "\nas Takuzu or Binairo."
          "\n\n© 2015"
          "\nq42.com * 0hh1.com")


def rules():
    print("Rules\n---------------"
          "\nThree adjacent tiles of the same character"
          "\nin a row or column isn't"
          "\nallowed."
          "\n\nRows and columns have an"
          "\nequal number of each character."
          "\n\nNo two rows and no two"
          "\ncolumns are the same."
          "\nYou can type in ' ' to make a tile blank.")


def apps():
    print("Apps\n---------------"
          "\nThe 01 h1 app is also free:"
          "\niOS"
          "\nAndroid"
          "\nWindows Phone"
          "\n\nThe source is on github:"
          "\ngithub.com/Q42/0hh1")


def other_games():
    print("\nGames"
          "\n---------------"
          "\nEnjoy our other games too!"
          "\n\n0h n0"
          "\nContranoid"
          "\nQuento"
          "\nNumolition"
          "\nFlippy Bit")









if __name__ == '__main__':
    opening_screen()
    start_page()