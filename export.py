import reports

with open(
    __file__.split("export.py")[0] + "export_report.txt", "r"
) as export_report:
    for line in export_report:
        year, genre, title, file_name = line.split("___")

with open(
    __file__.split("export.py")[0] + "export_report.txt", "w"
) as export_report:
    export_report.write(str(reports.count_games(file_name)) + "\n")
    export_report.write(str(reports.decide(file_name, year)) + "\n")
    export_report.write(str(reports.get_latest(file_name)) + "\n")
    export_report.write(str(reports.count_by_genre(file_name, genre)) + "\n")
    export_report.write(
        str(reports.get_line_number_by_title(file_name, title)) + "\n"
    )
    export_report.write(str(reports.sort_abc(file_name)) + "\n")
    export_report.write(str(reports.get_genres(file_name)) + "\n")
    export_report.write(str(reports.when_was_top_sold_fps(file_name)) + "\n")
