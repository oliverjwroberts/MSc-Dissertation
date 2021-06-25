from datetime import datetime


class Vehicle:
    def __init__(self, identifier, position):
        self.identifier = identifier # To Do: Check identifier is unique
        self.position = position
        #self.position = self.get_position()
        
    def __repr__(self):
        return f'{self.identifier}'
        
    
    def get_position(self):
        '''
        Function to get the vehicles location. For now this is a fixed 
        location. In the future, this could be from a GPS enabled device.        

        Returns
        -------
        position : Tuple of floats in order of latitude and then longitude
            Current position of vehicle.
        last_updated : String
            Date and time of the last positional update.

        '''
        position = (51.6189634, -3.8841088) # latitude, longitude for Bay Campus
        now = datetime.now()
        last_updated = now.strftime("%d/%m/%Y %H:%M:%S")
        return (position, last_updated)


class Helicopter(Vehicle):
    def __init__(self, identifier, position):
        super().__init__(identifier, position)
        self.type = 'Helicopter'
    
    
class RRV(Vehicle):
    def __init__(self, identifier, position):
        super().__init__(identifier, position)
        self.type = 'RRV'
        
        
class Fleet:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        
        
    def __repr__(self):
        return f'{self.name}, {self.vehicles}'
    
    
    def add_vehicle(self, vehicle_object):
        '''
        Function to add a vehicle to the fleet. 
        To Do: Check argument is infact a vehicle object.

        Parameters
        ----------
        vehicle_object : Vehicle class object
            A Vehicle class object decribing the type of vehicle to be
            added to the fleet.

        Returns
        -------
        None. Appends vehicle object to self.vehicles.

        '''
        self.vehicles.append(vehicle_object)
        
        
    def remove_vehicle(self, vehicle_identifier):
        '''
        Function to remove a vehicle from the fleet. 

        Parameters
        ----------
        vehicle_identifier : Vehicle class variable
            A Vehicle class variable able to identify the unique vehicle.

        Returns
        -------
        None. Removes vehicle from self.vehicles. 

        '''
        for vehicle in self.vehicles:
            if vehicle.identifier == vehicle_identifier:
                self.vehicles.remove(vehicle)
                
                
    def clear(self):
        '''
        Function to clear all vehicles from the fleet.
        To Do: Double check a user wants to do this. 

        Returns
        -------
        None. Overwrites self.vehicles as a new list.

        '''
        self.vehicles = []
        
        
class Emergency:
    def __init__(self, identifier, position):
        self.identifier = identifier
        self.position = position
        
        
    def __repr__(self):
        return f'{self.identifier}, {self.position}'
    
