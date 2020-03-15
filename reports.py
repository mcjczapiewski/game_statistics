import os

file_name = input("\nWhat's the name of a file with games data?\n\
Write it with it's extension, eg. game_stat.txt\n\
: ")
file_name = os.path.join(os.path.dirname(__file__), file_name)


def count_games(file_name):
    """How many games are in the file?"""
    number_of_games = 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                number_of_games += 1
    return number_of_games


def decide(file_name, year):
    """Is there a game from a given year?"""
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                game_year = int(line.split("\t")[2])
                if game_year == year:
                    return True
    return False


def get_latest(file_name):
    """Which was the latest game?"""
    latest_year = 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                game_year = int(line.split("\t")[2])
                if game_year > latest_year:
                    latest_year = game_year
        games_data.seek(0)
        for line in games_data:
            if "\t" + str(latest_year) + "\t" in line:
                return line.split("\t")[0]


def count_by_genre(file_name, genre):
    """How many games do we have by genre?"""
    number_by_genre = 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if line != "":
                game_genre = line.split("\t")[3]
                if game_genre == genre:
                    number_by_genre += 1
    return number_by_genre


def get_line_number_by_title(file_name, title):
    """What is the line number of the given game (by title)?"""
    with open(file_name, "r", encoding="utf-8") as games_data:
        for number, line in enumerate(games_data, 1):
            if title in line:
                return number
    raise ValueError


def sort_abc(file_name):
    """What is the alphabetical ordered list of the titles?"""
    list_of_games = []
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            list_of_games.append(line.split("\n")[0])
    while any(
        list_of_games[i] < list_of_games[i - 1]
        for i in range(1, len(list_of_games))
    ):
        for i in range(1, len(list_of_games)):
            if list_of_games[i] < list_of_games[i - 1]:
                list_of_games[i], list_of_games[i - 1] = (
                    list_of_games[i - 1],
                    list_of_games[i],
                )
    return list_of_games


def get_genres(file_name):
    """What are the genres?"""
    genres = []
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            game_genre = line.split("\t")[3]
            if game_genre not in genres:
                genres.append(game_genre)
    return sorted(genres)


def when_was_top_sold_fps(file_name):
    """What is the release date of the top sold "First-person shooter" game?"""
    top_fps_sold = 0.0
    top_fps_year = 0
    with open(file_name, "r", encoding="utf-8") as games_data:
        for line in games_data:
            if "First-person shooter" in line:
                total_sold = float(line.split("\t")[1])
                if total_sold > top_fps_sold:
                    top_fps_year = int(line.split("\t")[2])
        if top_fps_year != 0:
            return top_fps_year
    raise ValueError
