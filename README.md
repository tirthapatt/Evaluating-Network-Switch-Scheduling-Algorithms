# Network Switch Scheduling Algorithms Simulation

This repository contains Python simulations for evaluating different queuing architectures and scheduling algorithms in a 3x3 network switch.

## Prerequisites
You will need Python 3 installed, along with the `matplotlib` library for data visualization.

## How to Run
The project is completely modular. To run all simulations and generate the comparison graphs, 
Create the following six empty Python files inside this folder and copy the codes:


trace.py

fifo.py

voq_optimal.py

islip.py

visualize.py

main.py

execute the main script from your terminal:
python main.py

## Outputs
Running the script will output the step-by-step processing logs to the terminal. It will also generate and save two image files in the current directory:
1. `service_time_comparison.png`
2. `backlog_over_time.png`
