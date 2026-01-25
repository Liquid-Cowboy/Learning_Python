#!/usr/bin/env python3

from collections import Counter

numbs: list[int] = [1, 2, 2, 3, 4, 4, 42, 42, 42, 42, 42, 42, 42]

counter = Counter(numbs)

print(counter)
print()
print(counter.most_common())
print()

# prints the two most common
print(counter.most_common(2))
print()

# to get the least common, we have to invert that list
least_common = counter.most_common()[::-1]
print(least_common)
print()

# if a key doesn't exist, counter deals with it by
# creating it with the value of 0
print(counter['32'])
print()
print(counter[3])

# del + key to delete that entry
del counter[3]
print(counter[3])

# .update() takes an iterable object to update our counter object
counter.update([3, 3, 3])
print(counter[3])

counter2 = Counter([3, 42, 2, 33, 33])

print()
# if a key exists in both counter, the & operator
# will return the key/value pairs with the lowest count
print(counter & counter2)

# on the other hand, the or (|) operator will return the
# max key/value pairs regardless of wheter they exist in
# both keys or not
print(counter | counter2)
print()

# .elements() returns an iterator of elements, repeated as many times
# as their value (basically prints numbs again...)
print(list(counter.elements()))
print()
