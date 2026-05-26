import csv

def export_best_agent(report):

    best_agent = report["best_agent"]

    with open(
        "top_performer.csv",
        "w",
        newline=""
    ) as file:

        writer=csv.writer(file)

        writer.writerow([
            "Agent",
            "Packages Delivered",
            "Total Distance",
            "Efficiency"
        ])

        writer.writerow([
            best_agent,
            report[best_agent]["packages_delivered"],
            report[best_agent]["total_distance"],
            report[best_agent]["efficiency"]
        ])

    print(
        "CSV Exported Successfully"
    )