

from discrete_simulations import one_neighbor_spread_function, spread_discrete_rumour
from graph_generators import generate_ER_graph
import numpy as np
import matplotlib.pylab as plt
from continuous_simulations import spread_continuous_rumour


import networkx as nx
from networkx import Graph


from edge_expansion_simulation import spread_unit_edges_continuous_rumour
from display_simulations import display_simulation

print("STARTED SIMULATION")

# runs = [spread_discrete_rumour(generate_ER_graph, one_neighbor_spread_function, 40, 0) for i in range(3000)]
# run_length = [len(run) for run in runs]

# figure, ax = plt.subplots(figsize=(8,6))

# ax.hist(run_length, bins=40)

# events = spread_unit_edges_continuous_rumour(generate_ER_graph, 50, 0)

def ring_generator(number_of_nodes, timestep, informed_nodes) -> Graph:
    return nx.cycle_graph(number_of_nodes)

def shuffled_ring_generator(number_of_nodes, timestep, informed_nodes) -> Graph:
    node_permutation = np.random.permutation(number_of_nodes)
    return nx.cycle_graph(node_permutation)

events = spread_continuous_rumour(ring_generator, 20, enable_event_log=True)
anim = display_simulation(events)
anim.save('ring-simulation.mp4')

# plt.show()

print("END SIMULATION")