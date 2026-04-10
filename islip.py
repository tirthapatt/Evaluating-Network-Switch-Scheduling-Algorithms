# islip.py
from trace import get_arrivals

def simulate_voq_islip():
    print("\n--- PART 3: iSLIP VOQ Simulation ---")
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
            
        requests = {j: [] for j in range(3)}
        for src in range(3):
            for dst in range(3):
                if voq[src][dst]:
                    requests[dst].append(src)
                    
        grants = {i: [] for i in range(3)}
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
                    
        sent_this_slot = []
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
                    
                    grant_ptrs[accepted_dst] = (src + 1) % 3
                    accept_ptrs[src] = (accepted_dst + 1) % 3

        print(f"t={t}: iSLIP Sent {sent_this_slot} | Accept Ptrs: {accept_ptrs} | Grant Ptrs: {grant_ptrs}")
        t += 1

    print(f"iSLIP VOQ Total Service Time: t={t}")
    return t, backlog_over_time