# visualize.py
import matplotlib.pyplot as plt

def generate_graphs(fifo_time, fifo_log, opt_time, opt_log, islip_time, islip_log):
    plt.figure(figsize=(8, 5))
    labels = ['FIFO', 'Optimal VOQ', 'iSLIP VOQ']
    times = [fifo_time, opt_time, islip_time]
    plt.bar(labels, times, color=['red', 'green', 'blue'])
    plt.ylabel('Total Time Slots')
    plt.title('Total Service Time by Scheduling Algorithm')
    for i, v in enumerate(times):
        plt.text(i, v + 0.2, str(v), ha='center')
    plt.savefig('service_time_comparison.png')
    
    plt.figure(figsize=(10, 6))
    max_len = max(len(fifo_log), len(opt_log), len(islip_log))
    f_log = fifo_log + [0]*(max_len - len(fifo_log))
    o_log = opt_log + [0]*(max_len - len(opt_log))
    i_log = islip_log + [0]*(max_len - len(islip_log))
    time_slots = list(range(max_len))

    plt.plot(time_slots, f_log, marker='o', label='FIFO', color='red')
    plt.plot(time_slots, o_log, marker='s', label='Optimal VOQ', color='green')
    plt.plot(time_slots, i_log, marker='^', label='iSLIP VOQ', color='blue')
    
    plt.xlabel('Time Slots (t)')
    plt.ylabel('Total Number of Packets Remaining')
    plt.title('Backlog Over Time')
    plt.legend()
    plt.grid(True)
    plt.savefig('backlog_over_time.png')
    print("\nGraphs saved as 'service_time_comparison.png' and 'backlog_over_time.png'")