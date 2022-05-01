noise = input().split()
animals = ""
noises = {'Grr':'Lion', 'Rawr':'Tiger', 'Ssss':'Snake', 'Chirp':'Bird'}

for i in noise:
    animals += noises.get(i) + " "

print(animals)