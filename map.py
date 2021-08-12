import osmnx as ox


def generate_graph(place, network_type):
    '''
    Function to generate a graph from a place.
    TO DO: Clean the network, removing nodes that are not technically nodes.
    https://github.com/gboeing/osmnx-examples/blob/main/notebooks/04-simplify-graph-consolidate-nodes.ipynb

    Parameters
    ----------
    place : string
        A geocodable place.
    network_type : string {"all_private", "all", "bike", "drive", "drive_service", "walk"}
        What type of street network to retrieve.

    Returns
    -------
    graph : networkx.MultiDiGraph
        A networkx multidimensional graph of the chosen place.

    '''
    graph = ox.graph_from_place(place, network_type=network_type)
    
    # Impute speed (km/h) on all edges missing data
    graph = ox.add_edge_speeds(graph)
    
    # Calculate travel time (seconds) for all edges
    graph = ox.add_edge_travel_times(graph)    
    
    return graph


place = 'Swansea, Wales, UK'
network_type = 'drive'
graph = generate_graph(place, network_type)


# Save graph as GraphML file
ox.save_graphml(graph, 'graph.graphml')
    
