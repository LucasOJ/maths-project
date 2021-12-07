

from discrete_simulations import one_neighbor_spread_function, spread_discrete_rumour
from graph_generators import generate_ER_graph
import numpy as np
import matplotlib.pylab as plt

from edge_expansion_simulation import spread_unit_edges_continuous_rumour
from display_simulations import display_simulation

print("STARTED SIMULATION")

# runs = [spread_discrete_rumour(generate_ER_graph, one_neighbor_spread_function, 40, 0) for i in range(3000)]
# run_length = [len(run) for run in runs]

# figure, ax = plt.subplots(figsize=(8,6))

# ax.hist(run_length, bins=40)

events = spread_unit_edges_continuous_rumour(generate_ER_graph, 50, 0)

display_simulation(events)

# plt.show()

print("END SIMULATION")