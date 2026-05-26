import json
import math

def load_json(file_path):

    with open(file_path,'r') as file:
        return json.load(file)


def calculate_distance(point1,point2):

    x1,y1=point1
    x2,y2=point2

    return math.sqrt(
        (x2-x1)**2 + (y2-y1)**2
    )