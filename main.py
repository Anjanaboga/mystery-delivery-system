import json

from utils import load_json
from delivery import assign_packages
from delivery import simulate_delivery


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


print(
    "Report Generated Successfully"
)