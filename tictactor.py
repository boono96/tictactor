table = {"1": "_", "2": "_", "3": "_", "4": "_", "5": "_", "6": "_", "7": "_", "8": "_", "9": "_", }
xturn = True
useslot = []
turn = 0


def win(tablennumber, sectnum, thitnum):
    if table[tablennumber] != "_" and table[sectnum] != "_" and table[thitnum] != "_":
        if table[tablennumber] == "X" and table[sectnum] == "X" and table[thitnum] == "X":

            print("X win")
            print_board()
            return True

        elif table[tablennumber] == "O" and table[sectnum] == "O" and table[thitnum] == "O":

            print("O win")
            print_board()
            return True
    else:
        return False


def print_board():
    print(f"""
                                    ! {table["7"]} ! {table["8"]} ! {table["9"]} !\n 
                                    ! {table["4"]} ! {table["5"]} ! {table["6"]} !\n
                                    ! {table["1"]} ! {table["2"]} ! {table["3"]} !\n""")


notend = True
while notend:

    if xturn:
        print("X turn")
        slotinput = input("inputplace")
        if (slotinput not in useslot) and (slotinput.isdigit()) and not (int(slotinput) > 9):
            useslot.append(slotinput)
            table[slotinput] = "X"
            turn += 1
            xturn = False
    elif not xturn:
        print("O turn")
        slotinput = input("inputplace")
        if (slotinput not in useslot) and (slotinput.isdigit()) and not (int(slotinput) > 9):
            useslot.append(slotinput)
            table[slotinput] = "O"
            turn += 1
            xturn = True

    if turn > 3:
        # row
        if win("1", "2", "3"):
            break
        if win("4", "5", "6"):
            break
        if win("7", "8", "9"):
            break

        # column
        if win("7", "4", "1"):
            break
        elif win("8", "5", "2"):
            break
        if win("9", "6", "3"):
            break

        # cross
        if win("7", "5", "3"):
            break
        if win("1", "5", "9"):
            break

    print_board()

    if turn >= 9:
        print("draw")
        break
