dist_home = int(input())
rr_speed = int(input())
c_speed = int(input())

if dist_home // rr_speed >= (dist_home + 50) // c_speed:
    print("Yum")
else:
    print("Meep Meep")