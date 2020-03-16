import reports

with open(
    __file__.split("export.py")[0] + "export_report.txt", "r"
) as export_report:
    for line in export_report:
        title, file_name = line.split("___")

with open(
    __file__.split("export.py")[0] + "export_report.txt", "w"
) as export_report:
    export_report.write(str(reports.get_most_played(file_name)) + "\n")
    export_report.write(str(reports.sum_sold(file_name)) + "\n")
    export_report.write(str(reports.get_selling_avg(file_name)) + "\n")
    export_report.write(str(reports.count_longest_title(file_name)) + "\n")
    export_report.write(str(reports.get_date_avg(file_name)) + "\n")
    export_report.write(str(reports.get_game(file_name, title)) + "\n")
    export_report.write(str(reports.count_grouped_by_genre(file_name)) + "\n")
    export_report.write(str(reports.get_date_ordered(file_name)) + "\n")
