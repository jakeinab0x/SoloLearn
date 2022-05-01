yards = int(input())
def cheer(yards):
    if yards > 10:
        print("High Five")
    elif yards < 1:
        print("shh")
    else:
        print("Ra!" * yards)
        
cheer(yards)