import matplotlib.pyplot as plt
import matplotlib.animation as animation
from discrete_simulations import spread_discrete_rumour
from continuous_simulations import spread_continuous_rumour

from utils import draw_graph, generate_ER_graph
 

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