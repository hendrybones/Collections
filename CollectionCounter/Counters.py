from collections import Counter

# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

# Updating

coun = Counter()

coun.update([1, 2, 3, 1, 2, 1, 1, 2])
print(coun)

coun.update([1, 2, 4])
print(coun)