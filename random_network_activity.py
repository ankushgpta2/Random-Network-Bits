from numpy import random
import numpy
import numpy as np
import matplotlib.pyplot as plt
import math
import sympy
from sympy.matrices import randMatrix
from sympy import sin, cos, Matrix
from sympy.abc import rho, phi
import operator
import random
import statistics
import pandas
from numpy import linalg as LA
import clear
import turtle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification


NUMBER_OF_NODES = 100
average_values_of_nodes = []

# CODE FOR DOING A WEIGHTED DECISION TREE WITH MUTUAL INFORMATION
# RANDOMIZE THE WEIGHTS FOR THE NODES IN THE GRAPH AND THEN REORIENT THE NODES IN THE GRAPH ON THE BASIS OF
# WHERE THE MUTUAL INFORMATION IS MAXIMIZED (WHERE THIS IS RANDOMIZED AS WELL)

# Sample super simple decision tree
# ------------------------------------------- -------------------------------------------  ---------------------------->
# generating three different types of values (random)... (1) weight + (2) passed in value + (3) random noise from node

# random operator functions between weights and inputs and noise
for y in range(0, NUMBER_OF_NODES):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    operator_symbols = ('+', '-', '*', '/')
    rand_operators_for_input_weight_array = []
    weight_array = []
    input_array = []
    noise_array = []
    length = 1000

    for x in range(0, int(length)):
        rand_operators_for_input_weight_array.append(random.choice(tuple(ops)))
        weight_array.append(random.randint(0, 10000))
        input_array.append(np.random.randint(0, 10000))
        noise_array.append(random.uniform(0, 1))

    inputwithweightarray = []
    weightedinputwithnoisearray = []

    for x in range(0, int(length)):
        if rand_operators_for_input_weight_array[x] == "/" and weight_array[x] == 0:
            inputwithweight = input_array[x]
            inputwithweightarray.append(inputwithweight)
            weightedinputwithnoisearray.append(inputwithweight * noise_array[x])
        else:
            if rand_operators_for_input_weight_array[x] == "*" and weight_array[x] == 0:
                inputwithweight = input_array[x]
                inputwithweightarray.append(inputwithweight)
                weightedinputwithnoisearray.append(inputwithweight * noise_array[x])
            else:
                if rand_operators_for_input_weight_array[x] == "-" and (weight_array[x] - input_array[x]) * noise_array[x] \
                >= 5000:
                    inputwithweight = 5000
                    inputwithweightarray.append(inputwithweight)
                    weightedinputwithnoisearray.append(inputwithweight * noise_array[x])
                else:
                    inputwithweight = ops[rand_operators_for_input_weight_array[x]](input_array[x], weight_array[x])
                    if inputwithweight >= 5000:
                        inputwithweight = 5000
                        inputwithweightarray.append(inputwithweight)
                        weightedinputwithnoisearray.append(inputwithweight * noise_array[x])
                    else:
                        if inputwithweight < 0:
                            inputwithweight = abs(inputwithweight)
                            inputwithweightarray.append(inputwithweight)
                            weightedinputwithnoisearray.append(inputwithweight * noise_array[x])
                        else:
                            inputwithweightarray.append(inputwithweight)
                            weightedinputwithnoisearray.append(inputwithweight * noise_array[x])

# calculating the bit information value for each of the inputs

    bitvalue_array = []

    for x in range(0, len(weightedinputwithnoisearray)):
        float = weightedinputwithnoisearray[x]
        integer = math.floor(float)
        if float - integer > 0.5:
            integer = integer + 1
            try:
                integer = math.log(integer) / math.log(2)
                bitvalue_array.append(integer)
            except:
                integer = 0
                bitvalue_array.append(integer)
        else:
            try:
                integer = math.log(integer) / math.log(2)
                bitvalue_array.append(integer)
            except:
                integer = 0
                bitvalue_array.append(integer)

    print(bitvalue_array)

# sort the output bit values in order

    sorted_array = np.sort(bitvalue_array)
    xaxisvalues = range(0, len(sorted_array))

# take the average value of the node
    average = statistics.mean(sorted_array)
    average_values_of_nodes.append(average)
    x = range(0, len(average_values_of_nodes))
    plt.scatter(x, average_values_of_nodes)
    plt.title('original layout of average values')

plt.show()


                                                 # KNN FOR ALL THE NODES


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

# getting hypotenuse values for all the values between each other
for z in range(0, len(average_values_of_nodes)):
    # at this point a single x, y coordinate from the average array is passed to this next for loop
    x_coordinate_of_value_being_looked_at = count[0]
    y_coordinate_of_value_being_looked_at = average_values_of_nodes[0]
    for x in range(0, len(average_values_of_nodes)):
        x_coordinate_of_cycle_value = count[x] # just to store it into another variable for this particular loop
        y_coordinate_of_cycle_value = average_values_of_nodes[x] # just to store it into another variable for this particular loop
        x_difference_squared = (x_coordinate_of_value_being_looked_at - x_coordinate_of_cycle_value)**2
        y_difference_squared = (y_coordinate_of_value_being_looked_at - y_coordinate_of_cycle_value)**2
        hypotenuse = (x_difference_squared + y_difference_squared) ** 0.5
        hypotenuse_holder_old.append(hypotenuse)
    hypotenuse_holder_new = list(filter(lambda num: num != 0, hypotenuse_holder_old)) # remove zeros
    list.sort(hypotenuse_holder_new) # sort in increasing order
    for x in range(0, len(hypotenuse_holder_new)): # to get x and y coordinate
        if hypotenuse_holder_new[0] == hypotenuse_holder_old[x]:
            xcoordinate = x + z
            ycoordinate = average_values_of_nodes[x]
        else:
            a = 3
    x_value = [x_coordinate_of_value_being_looked_at, xcoordinate]
    y_value = [y_coordinate_of_value_being_looked_at, ycoordinate]
    plt.scatter(x_value, y_value)
    plt.plot(x_value, y_value)

    distance_array.append(hypotenuse)

# do some clearing
    list.clear(hypotenuse_holder_old) # clear the list for next iteration
    list.clear(hypotenuse_holder_new)
    list.clear(sorted_hypotenuse)

# restart some of the iteration for next round of values
    count.pop(0)
    average_values_of_nodes.pop(0) # remove the particular x value from the average list
    
plt.show()
total_distance = 0
for x in range(0, len(distance_array)-1):
    total_distance = distance_array[x] + distance_array[x + 1]
"""
plt.title('total distance of travel is...', total_distance)
"""
