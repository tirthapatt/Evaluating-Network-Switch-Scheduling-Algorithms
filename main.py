# main.py
from fifo import simulate_fifo
from voq_optimal import simulate_voq_optimal
from islip import simulate_voq_islip
from visualize import generate_graphs

if __name__ == "__main__":
    f_time, f_log = simulate_fifo()
    o_time, o_log = simulate_voq_optimal()
    i_time, i_log = simulate_voq_islip()
    
    generate_graphs(f_time, f_log, o_time, o_log, i_time, i_log)