# islip.py
from trace import get_arrivals

def simulate_voq_islip():
    print("\n--- PART 3: iSLIP VOQ Simulation (Multi-Iteration) ---")
    voq = {i: {j: [] for j in range(3)} for i in range(3)}
    grant_ptrs = {0: 0, 1: 0, 2: 0}
    accept_ptrs = {0: 0, 1: 0, 2: 0}
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
            
        # Track which ports are still available this time slot
        unmatched_inputs = set(range(3))
        unmatched_outputs = set(range(3))
        sent_this_slot = []
        
        # Run up to 3 iterations per time slot
        for iteration in range(3):
            # If everyone is matched, break the iteration loop early
            if not unmatched_inputs or not unmatched_outputs:
                break
                
            # 1. REQUEST Phase (Only unmatched ports participate)
            requests = {j: [] for j in unmatched_outputs}
            for src in unmatched_inputs:
                for dst in unmatched_outputs:
                    if voq[src][dst]:
                        requests[dst].append(src)
                        
            # 2. GRANT Phase
            grants = {i: [] for i in unmatched_inputs}
            for dst, req_srcs in requests.items():
                if req_srcs:
                    ptr = grant_ptrs[dst]
                    granted_src = None
                    for offset in range(3):
                        check_src = (ptr + offset) % 3
                        if check_src in req_srcs:
                            granted_src = check_src
                            break
                    if granted_src is not None:
                        grants[granted_src].append(dst)
                        
            # 3. ACCEPT Phase
            for src, grant_dsts in grants.items():
                if grant_dsts:
                    ptr = accept_ptrs[src]
                    accepted_dst = None
                    for offset in range(3):
                        check_dst = (ptr + offset) % 3
                        if check_dst in grant_dsts:
                            accepted_dst = check_dst
                            break
                    if accepted_dst is not None:
                        pkt = voq[src][accepted_dst].pop(0)
                        sent_this_slot.append(pkt["id"])
                        
                        # Update pointers (Modulo 3)
                        grant_ptrs[accepted_dst] = (src + 1) % 3
                        accept_ptrs[src] = (accepted_dst + 1) % 3
                        
                        # Remove matched ports from the available pool
                        unmatched_inputs.remove(src)
                        unmatched_outputs.remove(accepted_dst)

        print(f"t={t}: Multi-Iter iSLIP Sent {sent_this_slot} | Accept: {accept_ptrs} | Grant: {grant_ptrs}")
        t += 1

    print(f"Multi-Iter iSLIP VOQ Total Service Time: t={t}")
    return t, backlog_over_time
