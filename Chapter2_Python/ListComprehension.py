my_list = []

for i in range(5):
    my_list.append(i)

print(my_list)

my_list2 = [0, 1, 2, 3, 4]

# List Comprehension
# Was wird gespeichert (val- iterable)
my_list3 = [i for i in range(5)]
print(my_list3)

my_list4 = [i**2 for i in range(5)]
print(my_list4)

# Multi-dimensionale Liste
M = [[1, 2],
     [3, 4],
     [5, 6]]
print(M)

NUM_ROWS = 2
NUM_COLS = 3
M2 = [[i + j for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
print(M2)
