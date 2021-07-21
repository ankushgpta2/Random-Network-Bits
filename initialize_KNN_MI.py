# initializing variables + creating a bunch of storage arrays...

hypotenuse_holder_old = []  # for storing the hypotenuse values for a single value compared to all others
sorted_hypotenuse = [] # new array after sorting the values in increasing order

KNN_array = [] # used for then going through and determining the lowest value and the corresponding coordinates
count = [] # set up the x coordinate array
holding = [] # temporary array for holding values before transferring to final

for z in range(0, len(average_values_of_nodes)):
    count.append(z)

x_coordinate_of_value_being_looked_at = count[0]  # starting x, to initialize
y_coordinate_of_value_being_looked_at = average_values_of_nodes[0]  # starting y to initialize
xcoordinate2 = 0 # just to initialize
ycoordinate2 = 0 # just to initialize
xcoordinate = 0 # just to initialize
ycoordinate = 0 # just to initialize
x_coordinate_of_value_being_looked_at_next = 1
removalvalue = 0
distance_array = []
