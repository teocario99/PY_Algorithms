import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


myWeb = nx.DiGraph()
myPages = range(1, 5)

connections = [(1,3), (2,1), (2,3), (3,1), (3,2), (3,4), (4,5), (5,1), (5,4)]
myWeb.add_nodes_from(myPages)

pos = nx.shell_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
plt.show()

