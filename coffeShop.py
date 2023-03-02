from sequence.kernel.timeline import Timeline
from sequence.kernel.event import Event
from sequence.kernel.process import Process
import random
import matplotlib.pyplot as plt


class coffeShop(object):
    def __init__(self, tl: Timeline):
        self.timeline = tl
        self.doorEvents={}

    def customerIN(self, id):
        self.doorEvents[str(id)]={"in":"", "out":""}
        self.doorEvents[str(id)]["in"] = self.timeline.now()
        toGo =  random.choice([True, False])
        process = Process(self, 'customerOUT', [id])
        if toGo:
            event = Event(self.timeline.now() + 2, process)
        else:
            event = Event(self.timeline.now() + 10, process)
        self.timeline.schedule(event)

    def customerOUT(self, id):
        self.doorEvents[str(id)]["out"] = self.timeline.now()

tl = Timeline(60)
coffe_shop = coffeShop(tl)
customers = {"1":0,"2":3,"3":0,"4":5,"5":10,"6":3,"7":12,"8":5}
for customer in customers:
    id = customer
    timeIn = customers[customer]
    process = Process(coffe_shop, 'customerIN', [id])
    event = Event(timeIn, process)
    tl.schedule(event)
tl.run()
print(coffe_shop.doorEvents)
dict = coffe_shop.doorEvents
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
