import networkx as nx

def generate_ER_graph(number_of_nodes, timestep):
    return nx.erdos_renyi_graph(number_of_nodes, 1/500)

def generate_neighbor_graph(number_of_nodes, timestep):
    
    return nx.cycle_graph(number_of_nodes)