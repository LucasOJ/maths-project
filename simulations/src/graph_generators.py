import networkx as nx

def generate_ER_graph(timestep):
    return nx.erdos_renyi_graph(50, 1/50)