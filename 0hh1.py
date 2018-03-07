import time

#naming board spaces--------------------------------
#lol then i learned about enumerate. i made a program to type out all these variables though
a1 = " "
a2 = " "
a3 = " "
a4 = " "
a5 = " "
a6 = " "
a7 = " "
a8 = " "
a9 = " "
a10 = " "
a11 = " "
a12 = " "
b1 = " "
b2 = " "
b3 = " "
b4 = " "
b5 = " "
b6 = " "
b7 = " "
b8 = " "
b9 = " "
b10 = " "
b11 = " "
b12 = " "
c1 = " "
c2 = " "
c3 = " "
c4 = " "
c5 = " "
c6 = " "
c7 = " "
c8 = " "
c9 = " "
c10 = " "
c11 = " "
c12 = " "
d1 = " "
d2 = " "
d3 = " "
d4 = " "
d5 = " "
d6 = " "
d7 = " "
d8 = " "
d9 = " "
d10 = " "
d11 = " "
d12 = " "
e1 = " "
e2 = " "
e3 = " "
e4 = " "
e5 = " "
e6 = " "
e7 = " "
e8 = " "
e9 = " "
e10 = " "
e11 = " "
e12 = " "
f1 = " "
f2 = " "
f3 = " "
f4 = " "
f5 = " "
f6 = " "
f7 = " "
f8 = " "
f9 = " "
f10 = " "
f11 = " "
f12 = " "
g1 = " "
g2 = " "
g3 = " "
g4 = " "
g5 = " "
g6 = " "
g7 = " "
g8 = " "
g9 = " "
g10 = " "
g11 = " "
g12 = " "
h1 = " "
h2 = " "
h3 = " "
h4 = " "
h5 = " "
h6 = " "
h7 = " "
h8 = " "
h9 = " "
h10 = " "
h11 = " "
h12 = " "
i1 = " "
i2 = " "
i3 = " "
i4 = " "
i5 = " "
i6 = " "
i7 = " "
i8 = " "
i9 = " "
i10 = " "
i11 = " "
i12 = " "
j1 = " "
j2 = " "
j3 = " "
j4 = " "
j5 = " "
j6 = " "
j7 = " "
j8 = " "
j9 = " "
j10 = " "
j11 = " "
j12 = " "
k1 = " "
k2 = " "
k3 = " "
k4 = " "
k5 = " "
k6 = " "
k7 = " "
k8 = " "
k9 = " "
k10 = " "
k11 = " "
k12 = " "
l1 = " "
l2 = " "
l3 = " "
l4 = " "
l5 = " "
l6 = " "
l7 = " "
l8 = " "
l9 = " "
l10 = " "
l11 = " "
l12 = " "
#----------------------------------------------------------------
#----------------------------------------------------------------


def opening_screen():
    print("\n\n\n0h h1\na little logic game\nby Q42\nrewritten by Vanessa Nguyen :3\n")
    input("Press enter to begin:\n---------------\n")


def start_page():
    start_page_action = 0
    print("This is the menu\n---------------")
    print("1 - How to play\n2 - Play\n3 - Settings\n4 - About\n5 - Exit the game")
    start_page_action = input("---------------\nPlease type in the number corresponding to the action you wish to take:\n")

    #if their input wasn't a number or wasn't a number corresponding to an action, make them input till it's valid
    valid = False
    if start_page_action.isdigit():
        if (1 <= int(start_page_action)) or (int(start_page_action) <= 5):
            valid = True
    while not valid:
        start_page_action = input("Your input was invalid. Please type in the number corresponding to the action you wish to take:\n")
        if start_page_action.isdigit():
            if (int(start_page_action) < 1) or (5 < int(start_page_action)):
                start_page_action = input("Your input was invalid. Please type in the number corresponding to the action you wish to take:\n")
        if not start_page_action.isdigit():
                start_page_action = input("Your input was invalid. Please type in the number corresponding to the action you wish to take:\n")
        if (1 <= int(start_page_action)) and (int(start_page_action) <= 5):
            valid = True
    start_page_action = int(start_page_action)
    return start_action(start_page_action)


def start_action(start_page_action):
    action_input = start_page_action
    if action_input == 1:
        how_to_play()
    if action_input == 2:
        play()
    if action_input == 3:
        settings()
    if action_input == 4:
        about()
    if action_input == 5:
        print("Thank you for playing!")

def how_to_play():
    print("yay")

def play():
    valid = 0
    global size
    size = input("Select a size:\n4\n6\n8\n10\n12\n...\n")
    if (size == "4") or (size == "6") or (size == "8") or (size == "10") or (size == "12") or (size == "..."):
        valid = 1
    while not valid:
        size = input("The size you selected was not valid. Please try again:\n")
        if (size == "4") or (size == "6") or (size == "8") or (size == "10") or (size == "12") or (size == "..."):
            valid = 1
    if size == "4":
        play_board4()
    elif size == "6":
        board6()
    elif size == "8":
        board8()
    elif size == "10":
        board10()
    elif size == "12":
        board12()
    elif size == "...":
        games()


def play_board4():
    board4 = ["", a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4]
    start_time = time.time()
    incomplete = 1
    board_full = 0
    while incomplete:
        draw_board4()
        action4(board4, location4(), tile4())
    completion_message()
    if show_time == "Yes":
        time_taken = time.time() - start_time
        print(time_taken)


def draw_board4():
    board4 = ["", a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4, d1, d2, d3, d4]
    for i in range(1, 10):
        if (i == 1) or (i == 9):
            print("+---------------+")
        elif i%2 == 1:
            print("-----------------")
        elif i == 2:
            print("| " + board4[1] + " | " + board4[2] + " | " + board4[3] + " | " + board4[4] + " |")
        elif i == 4:
            print("| " + board4[5] + " | " + board4[6] + " | " + board4[7] + " | " + board4[8] + " |")
        elif i == 6:
            print("| " + board4[9] + " | " + board4[10] + " | " + board4[11] + " | " + board4[12] + " |")
        elif i == 8:
            print("| " + board4[13] + " | " + board4[14] + " | " + board4[15] + " | " + board4[16] + " |")


def location4():
    location = ""
    location = input("Where would you like to place your next tile (letter number, Ex. b3)?\n")

    #BROKEN
    #while location not in "a1 a2 a3 a4 b1 b2 b3 b4 c1 c2 c3 c4 d1 d2 d3 d4".split() or not board_full():
        #location = input("The location you chose is invalid, please re-choose your location:\n")
    return location


def tile4():
    tile = ""
    tile = input("Which tile would you like to place here (o or x)?\n")
    while (tile != "o") and (tile != "x"):
        tile = input("The tile type you chose is invalid, please re-choose your tile:\n")
    return tile

def xyz():
    """
    def action4(board4, location, tile):
    index = 0
    if location == a1:
        index = 1
    if location == a2:
        index = 2
    if location == a3:
        index = 3
    if location == a4:
        index = 4
    if location == b1:
        index = 5
    if location == b2:
        index = 6
    if location == b3:
        index = 7
    if location == b4:
        index = 8
    if location == c1:
        index = 9
    if location == c2:
        index = 10
    if location == c3:
        index = 11
    if location == c4:
        index = 12
    if location == d1:
        index = 13
    if location == d2:
        index = 14
    if location == d3:
        index = 15
    if location == d4:
        index = 16
    board4[index] = tile
    """
    pass

def action4(board4,location, tile):
    global a1
    global a2
    global a3
    global a4
    global b1
    global b2
    global b3
    global b4
    global c1
    global c2
    global c3
    global c4
    global d1
    global d2
    global d3
    global d4
    if location == "a1":
        a1 = tile
    if location == "a2":
        a2 = tile
    if location == "a3":
        a3 = tile
    if location == "a4":
        a4 = tile
    if location == "b1":
        b1 = tile
    if location == "b2":
        b2 = tile
    if location == "b3":
        b3 = tile
    if location == "b4":
        b4 = tile
    if location == "c1":
        c1 = tile
    if location == "c2":
        c2 = tile
    if location == "c3":
        c3 = tile
    if location == "c4":
        c4 = tile
    if location == "d1":
        d1 = tile
    if location == "d2":
        d2 = tile
    if location == "d3":
        d3 = tile
    if location == "d4":
        d4 = tile


def completion_message():
    pass

def board_full():
    pass


def board6():
    pass


def board8():
    pass

def board10():
    pass

def board12():
    pass




#default settings
show_time = "Yes"
show_hint = "Yes"

def settings():
    want_settings_changed = "1"
    while want_settings_changed == "1":
        print("\nSettings\n---------------\nShow elapsed time - " + show_time + "\nShow hint icon - " + show_hint)
        want_settings_changed = input("Press 1 if you would like to change your settings, otherwise press enter to go back:\n")
        while (want_settings_changed != "1") and (want_settings_changed != ""):
            want_settings_changed = input("Your input was invalid. Press 1 if you would like to change your settings, otherwise press enter to go back:\n")
        if want_settings_changed == "1":
            if show_time == "Yes" and show_hint == "Yes":
                time1_hint1()
            elif show_time == "Yes" and show_hint == "No":
                time1_hint0()
            elif show_time == "No" and show_hint == "Yes":
                time0_hint1()
            elif show_time == "No" and show_hint == "No":
                time0_hint0()
    start_page()


####################
# #time#_hint# functions are for changing the settings; 0=no, 1=yes for original setting
def time1_hint1():
    global show_hint
    global show_time
    change_setting = input("Type in 1 to change the elapsed time setting to No, 2 to change the hint setting to No, 3 to change both, or enter to continue without changes:\n")
    if change_setting == "1":
        show_time = "No"
        print("Your elapsed time setting has been changed to No")
    elif change_setting == "2":
        show_hint = "No"
        print("Your hint setting has been changed to No")
    elif change_setting == "3":
        show_time = "No"
        show_hint = "No"
        print("Your elapsed time and hint setting has been changed to No")
    else:
        print("No changes have been made")


def time1_hint0():
    global show_hint
    global show_time
    change_setting = input("Type in 1 to change the elapsed time setting to No, 2 to change the hint setting to Yes, 3 to change both, or enter to continue without changes:\n")
    if change_setting == "1":
        show_time = "No"
        print("Your elapsed time setting has been changed to No")
    elif change_setting == "2":
        show_hint = "Yes"
        print("Your hint setting has been changed to Yes")
    elif change_setting == "3":
        show_time = "No"
        show_hint = "Yes"
        print("Your elapsed time setting has been changed to No and hint setting has been changed to Yes")
    else:
        print("No changes have been made")


def time0_hint1():
    global show_hint
    global show_time
    change_setting = input("Type in 1 to change the elapsed time setting to Yes, 2 to change the hint setting to No, 3 to change both, or enter to continue without changes:\n")
    if change_setting == "1":
        show_time = "Yes"
        print("Your elapsed time setting has been changed to Yes")
    elif change_setting == "2":
        show_hint = "No"
        print("Your hint setting has been changed to No")
    elif change_setting == "3":
        show_time = "Yes"
        show_hint = "No"
        print("Your elapsed time setting has been changed to Yes and hint setting has been changed to No")
    else:
        print("No changes have been made")


def time0_hint0():
    global show_hint
    global show_time
    change_setting = input("Type in 1 to change the elapsed time setting to Yes, 2 to change the hint setting to Yes, 3 to change both, or enter to continue without changes:\n")
    if change_setting == "1":
        show_time = "Yes"
        print("Your elapsed time setting has been changed to Yes")
    elif change_setting == "2":
        show_hint = "Yes"
        print("Your hint setting has been changed to Yes")
    elif change_setting == "3":
        show_time = "Yes"
        show_hint = "Yes"
        print("Your elapsed time setting has been changed to No and hint setting has been changed to Yes")
    else:
        print("No changes have been made")
##########################


def about():
    print("\nAbout"
          "\n---------------"
          "\n0h h1 is a little logic game"
          "\nby Q42. It was created by"
          "\nMartin Kool."
          "\n\nThe concept is also known"
          "\nas Takuzu or Binairo."
          "\n\n© 2015"
          "\nq42.com * 0hh1.com")
    input("\nClick enter to continue:\n")
    rules()
    input("\nClick enter to continue:\n")
    print("Apps\n---------------"
          "\nThe 01 h1 app is also free:"
          "\niOS"
          "\nAndroid"
          "\nWindows Phone"
          "\n\nThe source is on github:"
          "\ngithub.com/Q42/0hh1")
    input("\nClick enter to continue:\n")
    input("\nClick enter to go back to menu:\n")
    games()
    start_page()

def games():
    print("\nGames"
          "\n---------------"
          "\nEnjoy our other games too!"
          "\n\n0h n0"
          "\nContranoid"
          "\nQuento"
          "\nNumolition"
          "\nFlippy Bit")

def rules():
    print("Rules\n---------------"
          "\nThree adjacent tiles of the same color"
          "\nin a row or column isn't"
          "\nallowed."
          "\n\nRows and columns have an"
          "\nequal number of each color."
          "\n\nNo two rows and no two"
          "\ncolumns are the same.")








if __name__ == '__main__':
    x = "start"
    opening_screen()
    start_page()