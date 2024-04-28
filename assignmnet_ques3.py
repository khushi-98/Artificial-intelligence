#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations

cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def calculate_cost(route):
    total_cost = 0
    for i in range(len(route)):
        j = (i + 1) % len(route)
        total_cost += cost_matrix[route[i]][route[j]]
    return total_cost

start_node = int(input("Enter the starting node (0-3): "))

all_routes = [route for route in permutations(range(4)) if route[0] == start_node]

shortest_route = None
shortest_cost = float('inf')
for route in all_routes:
    cost = calculate_cost(route)
    if cost < shortest_cost:
        shortest_route = route
        shortest_cost = cost

print("Shortest route:", end=" ")
for node in shortest_route:
    print(node, end=" ")
print("\nCost:", shortest_cost)


# In[ ]:




