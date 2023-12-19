import networkx as nx

#defining the nodes
nodes = ["S3A", "S3B", "S3G", "S3H", "S2C", "S2D", "S2I", "S1E", "S1L", "TC", "R1K", "R1M", "R2N", "R2O", "R3R", "R3S", "R3T"]
#defining the directed edges with their weights
edges = [
    ("S3A", "S2C", 1), ("S3B", "S2D", 3), ("S3G", "S2I", 1), ("S3H", "S2I", 2),
    ("S2C", "S1E", 2), ("S2C", "R1K", 1), ("S2D", "S1E", 2), ("S2I", "S1L", 4), ("S2I", "R1K", 6),
    ("S1E", "TC", 3), ("S1L", "TC", 6), 
    ("TC", "R1K", 4), ("TC", "R1M", 3),
    ("R1K", "R2N", 4), ("R1M", "R2O", 2), 
    ("R2N", "R3R", 1), ("R2N", "R3S", 5), ("R2O", "R3T", 4),
    ("R3S", "R3T", 2)
]

def compute_forman_ricci(G, edge):
    v1, v2 = edge
    w_e = G[v1][v2]['weight']

    # summation term
    summation_term = 0
    for e_v1 in G[v1]:
        for e_v2 in G[v2]:
            if e_v1 != e_v2 and G.has_edge(e_v1, e_v2):
                w_v1 = G[v1][e_v1]['weight']
                w_v2 = G[v2][e_v2]['weight']
                w_e_v1 = G[e_v1][e_v2]['weight']
                adj_vertices = (w_v1 / (w_e * (w_e_v1 ** 0.5))) + (w_v2 / (w_e * (w_e_v1 ** 0.5)))
                summation_term = summation_term + adj_vertices
                
    #Forman-Ricci curvature values
    ricci_curvature = w_e * ((w_v1 / w_e) + (w_v2 / w_e) - summation_term)
    return ricci_curvature

#creating a new graph
G = nx.Graph()
#adding the nodes
G.add_nodes_from(nodes)
#adding the weights
G.add_weighted_edges_from(edges)

#Forman-Ricci curvature values
forman_ricci_curvatures = {e: compute_forman_ricci(G, e) for e in G.edges}
forman_ricci_curvatures
