from networkx.classes.function import neighbors
from networkx.classes.graph import Graph
import random

def one_neighbor_spread_function(G: Graph, informed_nodes: set):
    # Can't mutate informed_nodes whilst iterating through it
    newly_informed_nodes = set()

    for informed_node in informed_nodes:
        neighbors = list(G.neighbors(informed_node))
        if len(neighbors) > 0:
            chosen_neighbor = random.choice(neighbors)
            newly_informed_nodes.add(chosen_neighbor)

    return informed_nodes.union(newly_informed_nodes)

def flooding_spread_function(G: Graph, informed_nodes: set):
    newly_informed_nodes = set()

    for informed_node in informed_nodes:
        neighbors = list(G.neighbors(informed_node))
        newly_informed_nodes = newly_informed_nodes.union(neighbors)

    return informed_nodes.union(newly_informed_nodes)

def spread_discrete_rumour(graph_generator, spread_function, number_of_nodes, initial_node):
    informed_nodes = {initial_node}
    timestep = 1
    events = []

    while len(informed_nodes) < number_of_nodes:
        G: Graph = graph_generator(number_of_nodes, timestep)
        assert(G.number_of_nodes() == number_of_nodes)
        
        informed_nodes: set = spread_function(G, informed_nodes)
        timestep += 1

        events.append({
            'timestep': timestep,
            'informed_nodes': informed_nodes,
            'graph': G
        })

    return events
