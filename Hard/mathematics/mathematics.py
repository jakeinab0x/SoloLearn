answer = int(input())
expressions = input().split()

def get_answer_index(answer, expressions):
    for i in expressions:
        if eval(i) == answer:
            return f"index {expressions.index(i)}"
    
    return "none"

print(get_answer_index(answer, expressions))