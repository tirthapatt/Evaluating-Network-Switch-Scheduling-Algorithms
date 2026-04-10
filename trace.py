# trace.py

packets_trace = [
    {"id": "p1", "t": 0, "src": 0, "dst": 0}, {"id": "p2", "t": 0, "src": 0, "dst": 1},
    {"id": "p3", "t": 0, "src": 1, "dst": 0}, {"id": "p4", "t": 0, "src": 1, "dst": 2},
    {"id": "p5", "t": 0, "src": 2, "dst": 0}, {"id": "p6", "t": 1, "src": 0, "dst": 2},
    {"id": "p7", "t": 1, "src": 2, "dst": 1}, {"id": "p8", "t": 2, "src": 1, "dst": 1},
    {"id": "p9", "t": 2, "src": 2, "dst": 2}, {"id": "p10", "t": 3, "src": 0, "dst": 1},
    {"id": "p11", "t": 3, "src": 1, "dst": 0}, {"id": "p12", "t": 3, "src": 2, "dst": 1},
    {"id": "p13", "t": 4, "src": 0, "dst": 0}, {"id": "p14", "t": 4, "src": 1, "dst": 2},
    {"id": "p15", "t": 4, "src": 2, "dst": 2}, {"id": "p16", "t": 5, "src": 0, "dst": 2},
    {"id": "p17", "t": 5, "src": 1, "dst": 1}, {"id": "p18", "t": 5, "src": 2, "dst": 0}
]

def get_arrivals(t):
    return [p for p in packets_trace if p["t"] == t]