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
