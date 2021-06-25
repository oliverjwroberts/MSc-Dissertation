from vehicles import RRV, Helicopter, Fleet, Emergency
import pandas as pd
import numpy as np
import osmnx as ox
import networkx as nx


# %% Geocode places and create  


# Places
singleton_hospital = ox.geocode('Singleton Hospital Swansea')
morriston_hospital = ox.geocode('Morriston Hospital Swansea')
premier_inn = ox.geocode('Premier Inn Swansea Waterfront')

# Create fleet
emrts_fleet = Fleet('EMRTS Fleet') 

# Add vehicles
emrts_fleet.add_vehicle(RRV('RRV1', singleton_hospital))
emrts_fleet.add_vehicle(Helicopter('Helo1', morriston_hospital))

# Create emergency
emergency = Emergency('EM1', premier_inn)


# %% Route Calculation


def get_routes(graph, fleet, emergency):
    
    def get_positions(fleet):
        # Get up-to-date positions of all vehicles
        for vehicle in fleet.vehicles:
            vehicle.get_position()
            
    # get_positions(fleet)
     
    routes = [] # Empty list to contain all routes

    # Find nearest node to emergency coordinates
    # Longitude then latitude for nearest_nodes function
    destination_node = ox.nearest_nodes(graph, emergency.position[1], emergency.position[0]) 

    # For each vehicle, work out route to emergency
    for vehicle in fleet.vehicles:
        
        # To Do: Add if statement for type of vehicle which determins how to calculate route
        # osmnx adds functionality to calculate euclidean distance: ox.distance.euclidean_dist_vec(y1, x1, y2, x2)

        # Find nearest node to vehicle coordinates
        origin_node = ox.nearest_nodes(graph, vehicle.position[1], vehicle.position[0]) 
    
        route = ox.shortest_path(graph, origin_node, destination_node, weight='travel_time')
        
        if route == None:
            print('No route found between nodes')
            routes.append('No route found')
        else:
            routes.append(route)

        
    print(f'Found routes for {len(fleet.vehicles)} vehicles in fleet')
        
    return routes

    
def get_route_attributes(graph, routes):
    
    length = [] # Empty list to contain total length
    travel_time = [] # Empty list to contain travel time
    
    for route in routes:
        cols = ['osmid', 'length', 'travel_time']
        attrs = ox.utils_graph.get_route_edge_attributes(graph, route)
        route_details = pd.DataFrame(attrs)[cols]
        
        length.append(route_details['length'].sum())
        travel_time.append(route_details['travel_time'].sum())
        
    return length, travel_time
        

# Load network graph generated from map.py
graph = ox.load_graphml('graph.graphml')

# Calculate route to emergency for each vehicle in fleet
routes = get_routes(graph, emrts_fleet, emergency)

# Get total length and travel time for each route
length, travel_time = get_route_attributes(graph, routes)

