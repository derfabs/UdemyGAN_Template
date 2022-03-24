import numpy as np

my_array = np.array([1, 2, 3], dtype=np.float32)
print(my_array)

my_zero_array = np.zeros(shape=(10), dtype=np.int32)
print(my_zero_array)

my_one_array = np.ones(shape=(3, 4), dtype=np.int32)
print(my_one_array)

my_reshaped_array = np.reshape(my_one_array, newshape=(12))
print(my_reshaped_array)

my_random_array = np.random.randint(low=0, high=11, size=10)
print(my_random_array)

my_random_array2 = np.random.randn(10)
print(my_random_array2)

print(my_random_array2.shape)
my_random_array2 = np.reshape(my_random_array2, newshape=(2, 5))
