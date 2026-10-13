# Creating strings
text = "Artificial Intelligence"
print("Original text:", text)

# Indexing and slicing
print("First letter:", text[0])
print("Last letter:", text[-1])
print("Slice [0:10]:", text[0:10])

# String methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("Intelligence", "Neural Networks"))

# Splitting and joining
words = text.split(" ")
print("Words list:", words)
print("Joined with hyphen:", "-".join(words))
