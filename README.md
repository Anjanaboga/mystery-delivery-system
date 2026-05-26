# Mystery Delivery System

Description:
A Python-based logistics simulator for FastBox delivery operations.

Features:
- Reads JSON data
- Assigns packages to nearest agents
- Simulates package delivery
- Calculates distance travelled
- Finds best performing agent
- Generates report.json

Assumptions:

1. Agents carry one package at a time.
2. Agent location updates after each delivery.
3. If two agents are at equal distance, first matching agent is selected.
4. Lower efficiency value indicates better performance.
Implemented Export to CSV functionality to generate a top_performer.csv file containing the best-performing delivery agent and related metrics.

How to Run:

python main.py