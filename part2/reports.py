def get_most_played(file_name):
    """What is the title of the most played game
    (i.e. sold the most copies)?"""
    most_copies = 0.0
    GAME_TITLE, COPIES_PER_GAME = 0, 1
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                game_copies = float(line.split("\t")[COPIES_PER_GAME])
                if game_copies > most_copies:
                    most_copies = game_copies
        games_data.seek(0)
        if str(most_copies).endswith(".0"):
            most_copies = int(most_copies)
        for line in games_data:
            if "\t" + str(most_copies) + "\t" in line:
                return line.split("\t")[GAME_TITLE]


def sum_sold(file_name):
    """How many copies have been sold total?"""
    total_copies = 0.0
    COPIES_PER_GAME = 1
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                total_copies += float(line.split("\t")[COPIES_PER_GAME])
    return total_copies


def get_selling_avg(file_name):
    """What is the average selling?"""
    total_copies = 0.0
    number_of_games = 0
    COPIES_PER_GAME = 1
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                number_of_games += 1
                total_copies += float(line.split("\t")[COPIES_PER_GAME])
    return total_copies / number_of_games


def count_longest_title(file_name):
    """How many characters long is the longest title?"""
    longest_title = 0
    GAME_TITLE = 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                this_title_length = sum(
                    1 for letter in line.split("\t")[GAME_TITLE]
                )
                if this_title_length > longest_title:
                    longest_title = this_title_length
    return longest_title


def get_date_avg(file_name):
    """What is the average of the release dates?"""
    total_copies = 0
    number_of_games = 0
    COPIES_PER_GAME = 2
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                number_of_games += 1
                total_copies += int(line.split("\t")[COPIES_PER_GAME])
    return round(total_copies / number_of_games)


def get_game(file_name, title):
    """What properties has a game?"""
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                if title in line:
                    a, b, c, d, e = line.split("\t")
                    return [a, float(b), int(c), d, e.split("\n")[0]]


def count_grouped_by_genre(file_name):
    """How many games are there grouped by genre?"""
    genres = {}
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            game_genre = line.split("\t")[3]
            if game_genre not in genres:
                genres[game_genre] = 1
            else:
                temp = genres[game_genre]
                temp += 1
                genres[game_genre] = temp
    return genres


def get_date_ordered(file_name):
    """What is the date ordered list of the games?"""
    list_of_games = []
    GAME_DATE, GAME_TITLE = 2, 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            list_of_games.append(
                line.split("\t")[GAME_DATE]
                + "_"
                + line.split("\t")[GAME_TITLE]
            )
    while any(
        list_of_games[i] > list_of_games[i - 1]
        for i in range(1, len(list_of_games))
    ):
        for i in range(1, len(list_of_games)):
            if list_of_games[i] > list_of_games[i - 1]:
                list_of_games[i], list_of_games[i - 1] = (
                    list_of_games[i - 1],
                    list_of_games[i],
                )
    GAME_DATE, GAME_TITLE = 0, 1
    while any(
        list_of_games[i].split("_")[GAME_DATE]
        == list_of_games[i - 1].split("_")[GAME_DATE]
        and list_of_games[i].split("_")[GAME_TITLE]
        < list_of_games[i - 1].split("_")[GAME_TITLE]
        for i in range(1, len(list_of_games))
    ):
        for i in range(1, len(list_of_games)):
            if (
                list_of_games[i].split("_")[GAME_DATE]
                == list_of_games[i - 1].split("_")[GAME_DATE]
                and list_of_games[i].split("_")[GAME_TITLE]
                < list_of_games[i - 1].split("_")[GAME_TITLE]
            ):
                list_of_games[i], list_of_games[i - 1] = (
                    list_of_games[i - 1],
                    list_of_games[i],
                )
    new_list = []
    for item in list_of_games:
        new_list.append(item.split("_")[GAME_TITLE])
    return new_list
