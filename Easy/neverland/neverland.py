"""
Visualise:

80 -> 10
   <- 10
60 -> 10
   <- 10
40 -> 10
   <- 10
20 -> 10
   <- 10
1  -> 10

"""

ppl = int(input()) + 1

def calc_time(ppl):
    trip = 10
    time = 0
    while ppl:
        if ppl < 20:
            time += trip
            return time
        elif ppl >= 20:
            ppl -= 20
            time += trip
            time += trip
    return time
      
print(calc_time(ppl))