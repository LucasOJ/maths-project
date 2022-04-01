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

def spread_discrete_rumour(graph_generator, number_of_nodes, initial_node=0, spread_function=flooding_spread_function, enable_event_log=False):
    informed_nodes = {initial_node}
    timestep = 0
    events = []

    while len(informed_nodes) < number_of_nodes:
        G: Graph = graph_generator(number_of_nodes, timestep, informed_nodes)
        assert(G.number_of_nodes() == number_of_nodes)
        
        informed_nodes: set = spread_function(G, informed_nodes)

        if enable_event_log:
            events.append({
                'timestep': timestep,
                'informed_nodes': informed_nodes,
                'graph': G,
                'activated_edge':(0,1)
            })
        timestep += 1

    if enable_event_log:
        assert(len(events) == timestep) 
        return events
    else:
        return timestep 
