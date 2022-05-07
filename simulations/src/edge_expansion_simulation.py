from networkx.classes.graph import Graph
import numpy as np
import random

from graph_generators import generate_ER_graph

def exponential_sample(rate: float):
    return np.random.exponential(1/rate)

def spread_unit_edges_continuous_rumour(graph_generator, number_of_nodes, initial_node):
    timestep = 0
    informed_nodes = {initial_node}
    events = []
    
    while len(informed_nodes) < number_of_nodes:

        G: Graph = graph_generator(number_of_nodes, timestep)

        number_of_edges = G.number_of_edges()

        round_time = exponential_sample(number_of_edges)

        # Uses memoryless property of exponential distribution
        while round_time < 1 and len(informed_nodes) < number_of_nodes:

            # The nth distribution attains the miniumum w.p lambda_n / sum_n lambda_n
            chosen_edge = random.choice(list(G.edges))
          
            informed_nodes = informed_nodes.union({chosen_edge[0], chosen_edge[1]})

            events.append({
                'time': timestep + round_time,
                'informed_nodes': informed_nodes,
                'graph': G
            })

            # Minumum of k exponentials has exponential distribution of sum of rates
            round_time += exponential_sample(number_of_edges)

        timestep += 1

    return events