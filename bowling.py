
# Returns the score value of the given single character string
# Valid characters:
#   - x, X, / = 10 points
#   - numbers (0-9) = 0-9 point(s)
# If the given character isn't valid the function throws ValueError
def get_value(char):
    try:
        return int(char)
    except ValueError:
        if char.lower() == "x" or char == "/":
            return 10
        elif char == '-':
            return 0
        raise ValueError()

# Calculates the game score:
# game: a list which contains single character strings
def score(game):
    result, frame = 0, 1
    in_first_half = True

    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])

            elif game[i].lower() == 'x':
                result += get_value(game[i+1])

                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])

        if not in_first_half:
            frame += 1

        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
        else:
            in_first_half = not in_first_half

    return result


"""


# Calculates the game score:
# game: a list which contains single character strings
def score(game):
    result, frame = 0, 0, 1
    in_first_half = True

    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - result += 10 - get_value(game[i - 1])
        else:
            result += get_value(game[i])

        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += get_value(game[i+1])

            elif game[i].lower() == "x":
                result += get_value(game[i+1])

                if game[i+2] == '/':
                    result += 10 - get_value(game[i+1])
                else:
                    result += get_value(game[i+2])


        if not in_first_half:
            frame += 1

        in_first_half = not in_first_half

        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1

    return result
"""