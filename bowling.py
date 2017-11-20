

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
# game_rolls: a list which contains single character strings
def score(game_rolls):
    result, current_frame, current_roll = 0, 1, 0
    in_first_half = True
    frame_limit = 10

    while current_frame <= frame_limit:
        result += get_value(game_rolls[current_roll])

        # Spare (Player knocks down all the pins in the second turn of his roll):
        # - Means the current frame value is the spare's value + the next roll's value, remove the previous first roll's score (since it added before check)
        if game_rolls[current_roll] == '/':
            result += get_value(game_rolls[current_roll + 1]) - get_value(game_rolls[current_roll - 1])

        # Strike (Player knocks down all the pins in the first turn of his frame, the frame is over since there are no more pins):
        # - Add the next 2 rolls' values to the score:
        elif game_rolls[current_roll].lower() == "x":
            result += get_value(game_rolls[current_roll + 2])

            # If the second roll after the strike is a spare, only add the spare's value:
            if game_rolls[current_roll + 2] != "/":
                result += get_value(game_rolls[current_roll + 1])
            in_first_half = False

        # Change frame:
        # - The player has 2 rolls (in a frame) to knock down as many pins as he can:
        if not in_first_half:
            in_first_half = True
            current_frame += 1
        else:
            in_first_half = False

        current_roll += 1
    return result
