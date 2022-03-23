import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from networkx.classes.graph import Graph
from discrete_simulations import flooding_spread_function, one_neighbor_spread_function, spread_discrete_rumour
from continuous_simulations import spread_continuous_rumour

from graph_generators import generate_ER_graph, generate_neighbor_graph
 
def make_colour_map(nodes, informed_nodes):
    return ['red' if i in informed_nodes else 'blue' for i in nodes]

def get_node_list(number_of_nodes):
    return [i for i in range(number_of_nodes)]

def display_simulation(events):
    figure, ax = plt.subplots(figsize=(8,6))

    def frame(i):
        ax.clear()
        event = events[i]
        G: Graph = event['graph']
        nodes = G.nodes
        activated_edge = event['activated_edge']

        informed_nodes: set = event['informed_nodes']
        colour_map = make_colour_map(nodes, informed_nodes)
        widths = [6 if sorted(edge) == sorted(activated_edge) else 1 for edge in G.edges]


        nx.draw_shell(G, node_color=colour_map, font_weight='bold', ax = ax, with_labels=True, font_color='white', width=widths)

    anim = animation.FuncAnimation(figure, frame, len(events), interval=200)
    return anim