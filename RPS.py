# Abbey seems to be the toughest opponent
# Looking at her code, she is using a Markov Chain to predict the next move
# We can use a similar approach, but instead of looking at the last two moves, we can look further back

# Like how Abbey used play_order with keys like "RR", "RP", etc. and a value that increments, we can do the same, just with longer strings
pattern_dict = {}

def player(prev_play, opponent_history=[]):
    global pattern_dict # Make 'global' so that pattern_dict can be modified while inside the function

    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    guess = "R"  # Default move

    if len(opponent_history) > 6: 
        last_six_moves = "".join(opponent_history[-6:])
        last_seven_moves = "".join(opponent_history[-(6+1):])

        # Update frequency count when a 7-move pattern is found
        pattern_dict[last_seven_moves] = pattern_dict.get(last_seven_moves, 0) + 1

        # Create all possible 7-move patterns by appending "R", "P", and "S" to the last six moves
        options = [last_six_moves + next_move for next_move in "RPS"]

        # If any of these sequences are not in the pattern_dict, initialize them to 0
        for option in options:
            if option not in pattern_dict:
                pattern_dict[option] = 0

        # Predict the next opponent move by finding the pattern with the highest frequency
        # Here, the last character of the pattern is the predicted move
        predict = max(options, key=lambda key: pattern_dict[key])
        predicted_next = predict[-1]

        # Map the predicted opponent move to the move that beats it
        counter = {"R": "P", "P": "S", "S": "R"}
        guess = counter[predicted_next]

    return guess
