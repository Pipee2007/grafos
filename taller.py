#Andrés Rodríguez
#Juan Plata

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

calles = [
    ("Inicio", "Gasolinera"),
    ("Gasolinera", "Ciudad"),
    ("Ciudad", "Valle"),
    ("Valle", "Gasolinera"),
    ("Gasolinera", "Peaje"),
    ("Peaje", "Destino"),
]

G.add_edges_from(calles)

posiciones = {
    "Inicio": (0, 1),
    "Gasolinera": (2, 1),
    "Ciudad": (3, 2),  
    "Valle": (3, 0),    
    "Peaje": (5, 1),
    "Destino": (7, 1),
}

plt.figure(figsize=(10, 5))

nx.draw_networkx_nodes(
    G, posiciones, node_size=2200, node_color="skyblue", edgecolors="navy"
)
nx.draw_networkx_labels(G, posiciones, font_size=9, font_weight="bold")

nx.draw_networkx_edges(
    G,
    posiciones,
    arrowstyle="->",
    arrowsize=18,
    edge_color="darkgreen",
    width=2,
)

plt.title("Red Vial con Rutas Alternativas")
plt.axis("off")
plt.tight_layout()

plt.show()