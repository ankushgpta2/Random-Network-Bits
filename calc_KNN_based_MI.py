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
    
