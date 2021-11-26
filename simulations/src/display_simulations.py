import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from networkx.classes.graph import Graph
from discrete_simulations import flooding_spread_function, one_neighbor_spread_function, spread_discrete_rumour
from continuous_simulations import spread_continuous_rumour

from graph_generators import generate_ER_graph, generate_neighbor_graph
 
def make_colour_map(number_of_nodes, informed_nodes):
    return ['red' if i in informed_nodes else 'blue' for i in get_node_list(number_of_nodes)]

def get_node_list(number_of_nodes):
    return [i for i in range(number_of_nodes)]

def display_simulation(events):
    figure, ax = plt.subplots(figsize=(8,6))

    def frame(i):
        ax.clear()
        event = events[i]
        G: Graph = event['graph']
        n = G.number_of_nodes()

        informed_nodes: set = event['informed_nodes']
        colour_map = make_colour_map(n, informed_nodes)

        nx.draw_shell(G, node_color=colour_map, font_weight='bold', with_labels=True, ax = ax)

    anim = animation.FuncAnimation(figure, frame, len(events), interval=500)
    plt.show()

print("STARTED SIMULATION")
events = spread_discrete_rumour(generate_neighbor_graph, one_neighbor_spread_function, 50, 0)
print("FINISHED SIMULATION")

display_simulation(events)