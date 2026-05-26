from utils import calculate_distance


def assign_packages(data):

    assignments={}

    for package in data["packages"]:

        warehouse=data["warehouses"][
            package["warehouse"]
        ]

        nearest_agent=None
        minimum_distance=float('inf')

        for agent,location in data["agents"].items():

            distance=calculate_distance(
                location,
                warehouse
            )

            if distance<minimum_distance:

                minimum_distance=distance
                nearest_agent=agent


        if nearest_agent not in assignments:
            assignments[nearest_agent]=[]

        assignments[nearest_agent].append(package)

    return assignments



def simulate_delivery(data,assignments):

    report={}

    agent_locations=data["agents"].copy()

    for agent in data["agents"]:

        report[agent]={

            "packages_delivered":0,
            "total_distance":0
        }


    for agent,packages in assignments.items():

        current_location=agent_locations[agent]

        for package in packages:

            warehouse=data["warehouses"][
                package["warehouse"]
            ]

            destination=package["destination"]

            pickup_distance=calculate_distance(
                current_location,
                warehouse
            )

            delivery_distance=calculate_distance(
                warehouse,
                destination
            )

            total=pickup_distance+delivery_distance

            report[agent]["packages_delivered"]+=1

            report[agent]["total_distance"]+=total

            current_location=destination


        agent_locations[agent]=current_location


    for agent in report:

        delivered=report[agent]["packages_delivered"]

        if delivered>0:

            report[agent]["total_distance"]=round(
                report[agent]["total_distance"],2
            )

            report[agent]["efficiency"]=round(
                report[agent]["total_distance"]/delivered,
                2
            )

        else:

            report[agent]["efficiency"]=0


    best=min(
        report,
        key=lambda x:
        report[x]["efficiency"]
        if report[x]["efficiency"]>0
        else float('inf')
    )

    report["best_agent"]=best

    return report