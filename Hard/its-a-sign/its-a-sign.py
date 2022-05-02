box_one = input()
box_two = input()
box_three = input()
box_four = input()

boxes = [box_one, box_two, box_three, box_four]

def find_palindrome(boxes):
    for box in boxes:
        if box == box[::-1]:
            return "Open"
    return "Trash"

print(find_palindrome(boxes))