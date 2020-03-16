import reports

file_name = input(
    "\nWhat's the name of a file with games data?\n\
Write it with it's extension, eg. game_stat.txt\n\
: "
)
file_name = __file__.split("printing.py")[0] + file_name

print(reports.get_most_played(file_name) + " is the most played game.")
print("Total number of all copies sold is " + str(reports.sum_sold(file_name)))
print("The average of selling is " + str(reports.get_selling_avg(file_name)))
print(
    "The longes title has "
    + str(reports.count_longest_title(file_name))
    + " characters"
)
print("The average release date is " + str(reports.get_date_avg(file_name)))
title = input("For what title would you like to know the game properties?\n: ")
print("  Game properties: " + str(reports.get_game(file_name, title)))
print("\nThese are the genres with number of games:")
for genre, number_of_games in reports.count_grouped_by_genre(
    file_name
).items():
    print(genre + ": " + str(number_of_games))
print(
    "\nThe date ordered list of games\n\
(from the newest to the oldest) looks like this:"
)
for item in reports.get_date_ordered(file_name):
    print(item)

with open(
    __file__.split("printing.py")[0] + "export_report.txt", "w"
) as write_out:
    write_out.write(title + "___" + file_name)
