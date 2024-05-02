import osmnx as ox
import networkx as nx
import numpy as np
from node import Node
import matplotlib.pyplot as plt

# ... (Node class definition from above)

def osm_to_adjacency_matrix(osm_file_path):
    G = ox.graph_from_xml(osm_file_path)

    # Create a dictionary to store Nodes
    nodes = {}
    for node, data in G.nodes(data=True):
        nodes[node] = Node(node, data['x'], data['y'])

    # Create the adjacency matrix
    adjacency_matrix = np.zeros((len(nodes), len(nodes)))

    # Calculate edge weights and add to the matrix
    for u, v, data in G.edges(data=True):
        weight = ox.distance.great_circle_vec(
            nodes[u].y_loc, nodes[u].x_loc, nodes[v].y_loc, nodes[v].x_loc
        )

        i = list(nodes.keys()).index(u)  # Find indices based on node IDs
        j = list(nodes.keys()).index(v)
        adjacency_matrix[i, j] = weight
        adjacency_matrix[j, i] = weight

    return adjacency_matrix, nodes  # Return both the matrix and the nodes dictionary


def plot_map(osm_file_path, adjacency_matrix, nodes=None):
    G = ox.graph_from_xml(osm_file_path)

    # Adjust positions if you're using the Node data structure
    if nodes:
        pos = {node: (node_obj.x_loc, node_obj.y_loc) for node, node_obj in nodes.items()}
    else:
        pos = nx.get_node_attributes(G, 'pos')  # Use layout positions from OSMnx

    # Customize edge weights 
    edge_weights = [adjacency_matrix[u, v] if adjacency_matrix[u, v] > 0 else 0.2 
                    for u, v in G.edges()]

    # Basic plot
    fig, ax = ox.plot_graph(G, node_size=0, edge_color='lightblue', edge_linewidth=edge_weights) 

    # More refined plot (optional)
    # ox.plot_graph_routes(G, routes, route_colors='r', route_linewidths=2, orig_dest_size=30, ax=ax) 

# Example usage
osm_file = 'map.osm' 
adjacency_matrix, nodes = osm_to_adjacency_matrix(osm_file)
plot_map(osm_file, adjacency_matrix, nodes)
plt.show()