import ast

def flatten(n):
    result = []
    for i in n:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

n = ast.literal_eval(input("Enter a nested list: "))
print("Single list:", flatten(n))