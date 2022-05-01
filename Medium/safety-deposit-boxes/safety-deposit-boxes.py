boxes = input().split(',')
target = input()

def drill(boxes, target):
    time = 0
    for i in boxes:
        if i == target:
            time += 5 
            break
        if boxes.index(i) < len(boxes):
            time += 5         
    return time
    
print(drill(boxes, target)) 