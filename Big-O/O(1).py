import time

small_array = ['nemo' for i in range(10)]
medium_array = ['nemo' for i in range(100)]
large_array = ['nemo' for i in range(100000)]

def finding_nemo(array):
  t0 = time.time()
  print(array[0]) # O(1)
  print(array[1]) # O(1)
  t1 = time.time()
  print(f'Time taken = {t1 - t0}')

finding_nemo(small_array)
finding_nemo(medium_array)
finding_nemo(large_array)