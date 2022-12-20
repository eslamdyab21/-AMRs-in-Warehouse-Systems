import pandas as pd
import numpy as np
import string


class Map2D():
    """
    Map2D class creates the 2d map with 2d numpy array, and because it's based on numpy 2d array
    the location's coordinates are based on numpy convention in indexing.

    :param size_x: width of the 2d grid
    :param size_x: height of the 2d grid
    """
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.map = np.zeros((size_y, size_x))
        self.map = self.map.astype('int')
        self.map = self.map.astype('object')



    def update_objects_locations(self, object_locations):
        """
        update_objects_locations function updates the locations of objects(robots or shelves) in the 2 grid.
        
        :param object_locations: dictionary of objects, each object has 2 attributes, the object name
                                 and a list of the object previous location and current location. 
                                 example: dict {R1:[prev_location, crrent_location], R2:[prev_location, crrent_location],.., Rn:[prev_location, crrent_location]}
        """

        for object_id, locations in object_locations.items():
            prev_location = locations[0]
            crrent_location = locations[1]

            # erase prev location
            pos_x = prev_location[0]
            pos_y = prev_location[1]
            self.map[pos_x][pos_y] = 0


            # add new location
            pos_x = crrent_location[0]
            pos_y = crrent_location[1]
            self.map[pos_x][pos_y] = object_id



    def show_map(self):
        """
        show_map function prints the 2d grid to visualize the movement of objects.
        """
        letters_seqence_columns = string.ascii_uppercase[0:self.size_x]
        letters_seqence_rows = string.ascii_uppercase[0:self.size_y]
        print(pd.DataFrame(self.map,columns=list(letters_seqence_columns),index=list(letters_seqence_rows)))
            
        print('---------------------------------------')




class Robot():
    """
    Robot class creates robots for the warehouse.

    :param id: (string) id for the robot to distinguish between robots 
    :param intial_location: (list) [x, y]
    :param intial_orientation: (string) robot's intial_orientation (up, down, right, left)
    :param speed: (float) robot speed
    :param map_size: (list) [map_size_x, map_size_y]

    :param 
    """
    def __init__(self, id, intial_location, intial_orientation, speed, map_size):
        
        self.id = None
        self.speed = speed
        # active_order_status: (boolean) if robot is delivering an order (paired with a shelf) it's true
        self.active_order_status = False 
        # paired_with_shelf_status: (boolean) if robot is paired with a shelf it's true
        self.paired_with_shelf_status = False
        self.paired_with_shelf = None
        self.battery_precentage = 100
        # cost: (float) robot's path cost from its current location to the shelf location
        self.cost = None
        self.orientation = intial_orientation
        self.map_size = map_size

        self.prev_location = intial_location
        self.current_location = intial_location
        self.locations = [self.prev_location, self.current_location]





# test the Map2D class
if __name__ == "__main__":
    map_size_x = 10
    map_size_y = 5

    map = Map2D(size_x=map_size_x, size_y=map_size_y)
    map.show_map()

    