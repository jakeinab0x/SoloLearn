my_name = input()
num_of_agents = int(input())
names = input().split()
names.append(my_name)
names = sorted(names)

names_with_agents = []

def time_until_licence(my_name, num_of_agents, names):
    time = 0
    i = 0
# If one agent available, we just find my_name in names (time complexity O(n))
    if num_of_agents == 1:
        for name in names:
            if name == my_name:
                time += 20
                return time            
            else:
                time += 20
    else:
# If more than one agent available, group names by number of agents (as if they are going to each of the agents' offices)
        while i < len(names):
            names_with_agents.append(names[:num_of_agents])
            del names[:num_of_agents]
            if len(names) == 1:
                names_with_agents.append(names)
            i += 1
# Find my_name within each index, adding 20 mins for each index checked
        for index in names_with_agents:
                if my_name in index:
                    time += 20
                    return time
                else:
                    time += 20
    
print(time_until_licence(my_name, num_of_agents, names))