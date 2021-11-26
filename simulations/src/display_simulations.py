import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from networkx.classes.graph import Graph
from discrete_simulations import spread_discrete_rumour
from continuous_simulations import spread_continuous_rumour

from graph_generators import generate_ER_graph
 
def make_colour_map(number_of_nodes, informed_nodes):
    return ['red' if i in informed_nodes else 'blue' for i in get_node_list(number_of_nodes)]

def get_node_list(number_of_nodes):
    return [i for i in range(number_of_nodes)]

def draw_graph(G: Graph, informed_nodes, ax):
    n = G.number_of_nodes()
    colour_map = make_colour_map(n, informed_nodes)
    nx.draw_shell(G, node_color=colour_map, with_labels=True, font_weight='bold', ax = ax)

def display_simulation(events):
    figure, ax = plt.subplots(figsize=(8,6))

    def frame(i):
        ax.clear()
        event = events[i]
        draw_graph(event['graph'], event['informed_nodes'], ax)

    anim = animation.FuncAnimation(figure, frame, len(events), interval=1000)
    plt.show()

events = spread_discrete_rumour(generate_ER_graph, 50, 0)


display_simulation(events)