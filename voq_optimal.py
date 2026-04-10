# voq_optimal.py
import itertools
from trace import get_arrivals

def simulate_voq_optimal():
    print("\n--- PART 2: VOQ Optimal Simulation ---")
    voq = {i: {j: [] for j in range(3)} for i in range(3)} 
    t = 0
    backlog_over_time = []
    
    while True:
        arrivals = get_arrivals(t)
        for p in arrivals:
            voq[p["src"]][p["dst"]].append(p)
            
        total_packets = sum(len(voq[i][j]) for i in range(3) for j in range(3))
        if t > 5 and total_packets == 0:
            break
        backlog_over_time.append(total_packets)

        if total_packets == 0:
            t += 1
            continue

        best_matching = []
        best_size = -1
        
        for p in itertools.permutations([0, 1, 2]):
            current_matching = []
            for src, dst in enumerate(p):
                if len(voq[src][dst]) > 0:
                    current_matching.append((src, dst))
            
            if len(current_matching) > best_size:
                best_size = len(current_matching)
                best_matching = current_matching

        sent_this_slot = []
        for src, dst in best_matching:
            pkt = voq[src][dst].pop(0)
            sent_this_slot.append(pkt["id"])
            
        print(f"t={t}: Optimal Matchings Sent {sent_this_slot}")
        t += 1

    print(f"Optimal VOQ Total Service Time: t={t}")
    return t, backlog_over_time