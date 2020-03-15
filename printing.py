import reports
# Printing functions

file_name = reports.file_name
# print(reports.count_games(file_name))
# year = input("What is the year you would like to check what game was released?")
# print(reports.decide(file_name, year))
# print(reports.get_latest(file_name))
# genre = input("From which genre would you like to count games?")
# print(reports.count_by_genre(file_name, genre))
# title = input("For what title would you like to know the line number?")
# print(reports.get_line_number_by_title(file_name, title))
for i in reports.sort_abc(file_name):
    print(i)
# print(reports.get_genres(file_name))
# print(reports.when_was_top_sold_fps(file_name))
