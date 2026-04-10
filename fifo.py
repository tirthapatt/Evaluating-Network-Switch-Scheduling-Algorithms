# fifo.py
from trace import get_arrivals

def simulate_fifo():
    print("\n--- PART 1: FIFO Queue Simulation ---")
    queues = [[], [], []]
    t = 0
    backlog_over_time = []
    
    while True:
        arrivals = get_arrivals(t)
        for p in arrivals:
            queues[p["src"]].append(p)
            
        total_packets = sum(len(q) for q in queues)
        if t > 5 and total_packets == 0:
            break
        backlog_over_time.append(total_packets)
        
        if total_packets == 0:
            t += 1
            continue

        heads = []
        for i in range(3):
            if queues[i]:
                heads.append((i, queues[i][0]))
                
        outputs_requested = {}
        for src, pkt in heads:
            dst = pkt["dst"]
            if dst not in outputs_requested:
                outputs_requested[dst] = []
            outputs_requested[dst].append((src, pkt))
            
        sent_this_slot = []
        for dst, requesters in outputs_requested.items():
            requesters.sort(key=lambda x: x[0]) 
            winner_src, winner_pkt = requesters[0]
            sent_this_slot.append(winner_pkt)
            queues[winner_src].pop(0)
            
        blocked_pkts = []
        for i in range(3):
            if queues[i]:
                head_pkt = queues[i][0]
                if head_pkt not in sent_this_slot:
                    for behind_pkt in queues[i][1:]:
                        if behind_pkt["dst"] not in outputs_requested:
                            blocked_pkts.append(behind_pkt["id"])
                            
        print(f"t={t}: Sent {[p['id'] for p in sent_this_slot]}")
        if blocked_pkts:
            print(f"  -> HoL Blocking detected! Packets stuck: {blocked_pkts}")
            
        t += 1
        
    print(f"FIFO Total Service Time: t={t}")
    return t, backlog_over_time