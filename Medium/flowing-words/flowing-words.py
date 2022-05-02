text = input().split()

def is_flowing(text):
    for i in text[::-1]:
        if i == text[0]:
            return "true"
        elif i[0] == text[text.index(i) - 1][-1]:
            continue
        else:
            return "false"
        
print(is_flowing(text))