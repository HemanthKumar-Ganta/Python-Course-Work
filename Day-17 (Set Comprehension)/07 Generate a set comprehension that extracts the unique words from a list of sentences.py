sentences = ["Python is easy", "Python is powerful", "Coding is fun"]

s = {word for sentence in sentences for word in sentence.split()}

print(s)