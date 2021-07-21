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
