import json

from utils import load_json
from delivery import assign_packages
from delivery import simulate_delivery
from bonus.export_csv import export_best_agent


data=load_json("data.json")

assignments=assign_packages(data)

report=simulate_delivery(
    data,
    assignments
)

with open(
    "report.json",
    "w"
) as file:

    json.dump(
        report,
        file,
        indent=4
    )
    export_best_agent(report)


print(
    "Report Generated Successfully"
)