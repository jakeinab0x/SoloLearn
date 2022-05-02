B = int(input())
R = int(input())
G = int(input())
Y = int(input())
blocks = [B,R,G,Y]
divided = [i % 15 for i in blocks]
print(sum(divided))