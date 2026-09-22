import matplotlib.pyplot as plt
import networkx as nx

# 1. Configuración del Grafo (Red Ambiental Galápagos)
G = nx.Graph(nombre="Red Ambiental Galápagos", region="Pacífico Este")

# Nodos: Estaciones de monitoreo marino
G.add_nodes_from(
    [
        ("Santa Cruz", {"tipo": "Base Central", "personal": 25}),
        ("Isabela", {"tipo": "Volcánica/Reserva", "personal": 12}),
        ("San Cristóbal", {"tipo": "Investigación", "personal": 18}),
        ("Floreana", {"tipo": "Costera", "personal": 8}),
        ("Fernandina", {"tipo": "Santuario Marino", "personal": 5}),
        ("Española", {"tipo": "Observatorio Biol.", "personal": 10}),
    ]
)

# Aristas: Rutas marítimas entre estaciones
G.add_edges_from(
    [
        ("Santa Cruz", "Isabela", {"distancia_mili": 45, "transporte": "Lancha Rápida"}),
        ("Isabela", "Fernandina", {"distancia_mili": 20, "transporte": "Bote Solar"}),
        ("Fernandina", "Santa Cruz", {"distancia_mili": 55, "transporte": "Catamarán"}),
        ("Santa Cruz", "San Cristóbal", {"distancia_mili": 50, "transporte": "Ferry de Carga"}),
        ("San Cristóbal", "Española", {"distancia_mili": 30, "transporte": "Lancha Rápida"}),
        ("Española", "Floreana", {"distancia_mili": 35, "transporte": "Bote Solar"}),
        ("Floreana", "Santa Cruz", {"distancia_mili": 25, "transporte": "Catamarán"}),
        ("Isabela", "Floreana", {"distancia_mili": 40, "transporte": "Lancha Rápida"}),
    ]
)


def camino_hamilton(g, p=[]):
    """Encuentra un Camino de Hamilton recurriendo la red."""
    if not p:
        return next((r for n in g if (r := camino_hamilton(g, [n]))), None)
    if len(p) == len(g):
        return p
    for vec in g[p[-1]]:
        if vec not in p and (r := camino_hamilton(g, p + [vec])):
            return r


nodos = list(G.nodes)
matriz = nx.to_numpy_array(G, weight=None, dtype=int)
ruta = camino_hamilton(G)

# 2. Impresión de consola formateada
print(f"MONITOREO OCEANOGRÁFICO - {G.graph['nombre'].upper()}\n")
print(
    "[1] MATRIZ DE ADYACENCIA\n              "
    + "".join(f"{n[:9]:>11}" for n in nodos)
)
for i, fila in enumerate(matriz):
    print(f"{nodos[i]:<14}" + "".join(f"{v:>11}" for v in fila))

print(
    "\n[2] ESTACIONES DE INVESTIGACIÓN Y RUTAS\nEstaciones:\n"
    + "\n".join(
        f"  • {k:<14} | Tipo: {v['tipo']:<20} | Personal: {v['personal']} científicos"
        for k, v in G.nodes(data=True)
    )
)
print(
    "\nRutas Marítimas:\n"
    + "\n".join(
        f"  • {u:<13} ↔ {v:<13} | Vía: {d['transporte']:<16} | Distancia: {d['distancia_mili']} MN"
        for u, v, d in G.edges(data=True)
    )
)

print("\n[3] RUTA RECOMENDADA DE RELLENADO DE SUMINISTROS (CAMINO DE HAMILTON)")
if ruta:
    print(
        "Secuencia de Visita:\n"
        + "\n".join(f"  Paso {i+1}: {nodo}" for i, nodo in enumerate(ruta))
    )
    print("\nTrayecto en Anillo:\n  " + " ➔ ".join(ruta))

# 3. Personalización visual avanzada (Tema Oscuro / Neón Marino)
plt.style.use("dark_background")
fig, ax = plt.subplots(figsize=(10, 7), facecolor="#0B132B")
ax.set_facecolor("#0B132B")

# Posicionamiento semiorgánico mediante algoritmo Shell
pos = nx.shell_layout(G)

# Dibujar aristas base (líneas finas cian pálido)
nx.draw_networkx_edges(
    G, pos, ax=ax, edge_color="#1C2541", width=2, style="dashed"
)

# Dibujar el Camino de Hamilton resaltado (Verde Neón deslumbrante)
if ruta:
    aristas_ham = list(zip(ruta[:-1], ruta[1:]))
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=aristas_ham,
        ax=ax,
        width=4.5,
        edge_color="#00FFAB",  # Verde neón
        alpha=0.9,
    )

# Dibujar nodos con gradiente visual (Azul Turquesa Neón con borde cian)
nx.draw_networkx_nodes(
    G,
    pos,
    ax=ax,
    node_color="#00B4D8",
    node_size=3200,
    edgecolors="#90E0EF",
    linewidths=2.5,
)

# Etiquetas de los nodos
nx.draw_networkx_labels(
    G,
    pos,
    ax=ax,
    font_size=10,
    font_weight="bold",
    font_color="#FFFFFF",
    font_family="sans-serif",
)

# Etiquetas de las aristas
labels = {
    (u, v): f"{d['transporte']}\n({d['distancia_mili']} MN)"
    for u, v, d in G.edges(data=True)
}
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=labels,
    font_size=7.5,
    font_color="#CAF0F8",
    bbox=dict(boxstyle="round,pad=0.3", fc="#0B132B", ec="#1C2541", lw=1),
)

plt.title(
    "Ruta de Monitoreo Ambiental - Camino de Hamilton (Verde Neón)",
    fontsize=14,
    color="#90E0EF",
    pad=15,
    weight="bold",
)
plt.axis("off")
plt.tight_layout()
plt.savefig("grafo_galapagos.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor="none")
print("\nImagen guardada correctamente como 'grafo_galapagos.png'")

try:
    plt.show()
except Exception:
    pass