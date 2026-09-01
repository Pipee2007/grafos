import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_edge("Carlos", "Elena", relacion="pareja")

G.add_edge("Carlos", "Ana", relacion="padre")
G.add_edge("Elena", "Ana", relacion="padre")
G.add_edge("Carlos", "Luis", relacion="padre")
G.add_edge("Elena", "Luis", relacion="padre")

G.add_edge("Ana", "Pedro", relacion="pareja")
G.add_edge("Luis", "Laura", relacion="pareja")

G.add_edge("Ana", "Mateo", relacion="padre")
G.add_edge("Pedro", "Mateo", relacion="padre")
G.add_edge("Luis", "Sofia", relacion="padre")
G.add_edge("Laura", "Sofia", relacion="padre")

posiciones = {
    "Carlos": (1, 2),
    "Elena": (2, 2),
    "Pedro": (4, 1),
    "Ana": (2, 1),
    "Luis": (5, 1),
    "Laura": (7, 1),
    "Mateo": (3, 0),
    "Sofia": (6, 0),
}

aristas_pareja = [
    (u, v) for u, v, d in G.edges(data=True) if d["relacion"] == "pareja"
]
aristas_padre = [
    (u, v) for u, v, d in G.edges(data=True) if d["relacion"] == "padre"
]

plt.figure(figsize=(10, 6))

nx.draw_networkx_nodes(
    G, posiciones, node_size=2200, node_color="skyblue", edgecolors="navy"
)
nx.draw_networkx_labels(G, posiciones, font_size=10, font_weight="bold")

nx.draw_networkx_edges(
    G,
    posiciones,
    edgelist=aristas_padre,
    arrowstyle="->",
    arrowsize=15,
    edge_color="gray",
    width=2,
)

nx.draw_networkx_edges(
    G,
    posiciones,
    edgelist=aristas_pareja,
    arrowstyle="-",
    edge_color="red",
    style="dashed",
    width=2,
)

plt.title("Árbol Genealógico")
plt.axis("off")
plt.tight_layout()

plt.show()