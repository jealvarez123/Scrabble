letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
           "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {
    key: value
    for key, value
    in zip(letters, points)}
letter_to_points[" "] = 0


# letter_to_points.setdefault(char.upper(), 0)
# def score_word(word): return sum([letter_to_points.get(char.upper(), 0) for char in word])
# This is an example of what I can do later to improve the code

# This turns the words into points
def score_word(word):
    point_total = 0
    for letter in word:
        # This makes all the words entered upper case
        letter = letter.upper()
        point_total += letter_to_points.get(letter, 0)
    return point_total


# example
brownie_points = score_word("BROWNIE")
# print(brownie_points)

# this is a sample list of players
player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'LexiCon': ['ERASER', 'BELLY', 'HUSKY'],
    'ProfReader': ['ZAP', 'COMA', 'PERIOD']
}

# This holds the players and points added up
player_to_points = {}

# this adds all the points of each player
def update_point_totals():
    for key, value in player_to_words.items():
        # print(value)
        player_points = 0
        for words in value:
            player_points += score_word(words)
            player_to_points[key] = player_points
    return player_to_points


update_point_totals()


# This will add a new word to the player plays it
def play_word(player, word):
    player_to_points[player] = player_to_points.get(player) + score_word(word)
    return player_to_points

# example of added a word
print(play_word('player1', 'Zebra'))
