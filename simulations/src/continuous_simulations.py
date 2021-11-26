from networkx.classes.graph import Graph
import numpy as np
import random

def exponential_sample(rate: float):
    return np.random.exponential(1/rate)

# TODO: Think about when to use G_0 or G_1

def spread_continuous_rumour(graph_generator, number_of_nodes, initial_node):
    timestep = 0
    informed_nodes = {initial_node}
    events = []
    
    while len(informed_nodes) < number_of_nodes:

        G: Graph = graph_generator(timestep)
        assert(G.number_of_nodes() == number_of_nodes)

        round_time = exponential_sample(number_of_nodes)

        # Uses memoryless property of exponential distribution
        while round_time < 1 and len(informed_nodes) < number_of_nodes:

            # The nth distribution attains the miniumum w.p lambda_n / sum_n lambda_n
            chosen_node = random.choice(list(G.nodes))
            neighbors = list(G.neighbors(chosen_node))
            if len(neighbors) > 0:
                chosen_neighbor = random.choice(neighbors)

                chosen_informed = chosen_node in informed_nodes
                neighbor_informed = chosen_neighbor in informed_nodes

                if (chosen_informed and not neighbor_informed) or (neighbor_informed and not chosen_informed):
                    informed_nodes.add(chosen_node)
                    informed_nodes.add(chosen_neighbor)
            
            events.append({
                'time': timestep + round_time,
                'informed_nodes': set(informed_nodes),
                'graph': G
            })


            # Minumum of k exponentials has exponential distribution of sum of rates
            round_time += exponential_sample(number_of_nodes)

        timestep += 1

    return events
            
