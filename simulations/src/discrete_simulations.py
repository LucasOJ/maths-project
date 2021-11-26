from networkx.classes.graph import Graph
import random


def spread_discrete_rumour(graph_generator, number_of_nodes, initial_node):
    informed_nodes = {initial_node}
    timestep = 1
    events = []

    while len(informed_nodes) < number_of_nodes:
        G: Graph = graph_generator(timestep)
        assert(G.number_of_nodes() == number_of_nodes)

        newly_informed_nodes = set()
        for informed_node in informed_nodes:
            neighbors = list(G.neighbors(informed_node))
            if len(neighbors) > 0:
                chosen_neighbor = random.choice(neighbors)
                newly_informed_nodes.add(chosen_neighbor)
        
        timestep += 1
        informed_nodes = informed_nodes.union(newly_informed_nodes)

        events.append({
            'timestep': timestep,
            'newly_informed_nodes': newly_informed_nodes,
            'informed_nodes': informed_nodes,
            'graph': G
        })

    return events
