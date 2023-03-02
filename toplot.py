import matplotlib.pyplot as plt

# Sample dictionary
dict = {'1': {'in': 0, 'out': 10}, '3': {'in': 1, 'out': 11}, '6': {'in': 3, 'out': 5}, '2': {'in': 3, 'out': 13}, '8': {'in': 5, 'out': 7}, '4': {'in': 5, 'out': 7}, '5': {'in': 10, 'out': 20}, '7': {'in': 12, 'out': 22}}

# Sort the keys of the dictionary
sorted_ids = sorted(dict.keys())

# Create lists to store y values
y = []

# Iterate over the sorted keys of the dictionary and append the id to the y list
for id in sorted_ids:
    y.append(id)

# Plot the in and out times for each id using horizontal lines with colored edges
for id in sorted_ids:
    plt.hlines(y=id, xmin=dict[id]['in'], xmax=dict[id]['out'], linewidth=2)
    plt.plot(dict[id]['in'], id, 'go', label='In Time')
    plt.plot(dict[id]['out'], id, 'ro', label='Out Time')

# Set the x and y axis labels
plt.xlabel('in and out Times')
plt.ylabel('Customer ID')

# Set the plot title
plt.title('In and Out Times for each Customer')

# Show the plot
plt.show()
