words = ["apple", "cat", "banana", "dog", "apple", "kiwi", "grapes"]
s = {i for i in words if len(i) > 3}
print(s)