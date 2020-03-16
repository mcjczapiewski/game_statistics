import reports

file_name = reports.file_name

print(
    "\nThere are "
    + str(reports.count_games(file_name))
    + " games in the file."
)
year = input(
    "What is the year you would like to check if any \
game was released?\n: "
)
print(
    "  The statenemt that there was a game released in year "
    + str(year)
    + " is "
    + str(reports.decide(file_name, year))
)
print("The latest game title is " + str(reports.get_latest(file_name)))
genre = input("From which genre would you like to count games?\n: ")
print(
    "  There are " + str(reports.count_by_genre(file_name, genre)),
    genre + " games.",
)
title = input("For what title would you like to know the line number?\n: ")
print(
    "  This game is in line number "
    + str(reports.get_line_number_by_title(file_name, title))
)
print("\nThis is your list in alphabetical order:")
for item in reports.sort_abc(file_name):
    print(item)
print("\nThese are the genres contained in the file:")
for item in reports.get_genres(file_name):
    print(item)
print(
    "\nTop sold FPS was released in "
    + str(reports.when_was_top_sold_fps(file_name))
)

with open(
    __file__.split("printing.py")[0] + "export_report.txt", "w"
) as write_out:
    write_out.write(str(year) + "_" + genre + "_" + title)
