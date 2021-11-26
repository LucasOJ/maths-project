import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.graph import Graph

def make_colour_map(number_of_nodes, informed_nodes):
    return ['red' if i in informed_nodes else 'blue' for i in get_node_list(number_of_nodes)]

def get_node_list(number_of_nodes):
    return [i for i in range(number_of_nodes)]

def draw_graph(G: Graph, informed_nodes, ax):
    n = G.number_of_nodes()
    colour_map = make_colour_map(n, informed_nodes)
    nx.draw_shell(G, node_color=colour_map, with_labels=True, font_weight='bold', ax = ax)

def generate_ER_graph(timestep):
    return nx.erdos_renyi_graph(50, 1/200)